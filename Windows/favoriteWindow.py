from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Windows.manualAddDialog import *

from Windows.centralWindow import *
from Windows import favoriteWindow_ui
from Util import constants, scroller
from Util.enums import *
from Util.SqlTableModel import *
from Util.SqlTileTableModel import *

class CategoryTab():
    __slots__ = ['widget', 'horizontalLayout', 'listView', 'listModel']
    def __init__(self, widget = None, horizontalLayout = None, listView = None, listModel = None):
        self.widget = widget
        self.horizontalLayout = horizontalLayout
        self.listView = listView
        self.listModel = listModel

class FavoriteWindow(QWidget, favoriteWindow_ui.Ui_FavoriteWindow):
    def __init__(self, centralWindow, config, dbManager, parent=None):
        super(FavoriteWindow, self).__init__(parent)
        self.setupUi(self)

        self.centralWindow = centralWindow
        self.config = config
        self.dbManager = dbManager

        self.favoritesTabModel = SqlTileTableModel(self.dbManager.connection, 'inventory', 'favorites_index',
                                                    Qt.AscendingOrder, 'favorites_index IS NOT NULL', (1,), ('name',))

        # Set Favorite's View to have model
        self.favoritesTableView.setModel(self.favoritesTabModel)
        # Setup kinetic scrolling on favorite's table view (can use touchscreen to flick and scroll like on phones)
        scroller.setupScrolling(self.favoritesTableView)
        # Connect selectItem function to the selectionChanged signal that is triggered when an item is deselected or
        # selected
        self.favoritesTableView.selectionModel().selectionChanged.connect(self.selectItem)

        # Create an empty tabDict which will contain a dictionary for each tab in the window, query all categories and
        # add each tab to the window
        self.tabDict = {}
        self.categories = self.dbManager.GetCategories(True)
        for category in self.categories:
            self.addTab(category['id'], category['name'])

        # Enable the add and remove button because they are only shown when items are selected on the current tab
        self.addBtn.setEnabled(False)
        self.removeBtn.setEnabled(False)

    def addTab(self, id, name):
        newTab = CategoryTab(QWidget(self.categoryTabWidget))
        newTab.horizontalLayout = QHBoxLayout(newTab.widget)
        newTab.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        # Create list view for category and with the appropiate settings
        newTab.listView = QListView(newTab.widget)
        font = QFont()
        font.setPointSize(21)
        newTab.listView.setFont(font)
        newTab.listView.setFrameShape(QFrame.NoFrame)
        newTab.listView.setFrameShadow(QFrame.Plain)
        newTab.listView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        newTab.listView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        newTab.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        newTab.listView.setDragDropMode(QAbstractItemView.DragDrop)
        newTab.listView.setDefaultDropAction(Qt.ActionMask)
        newTab.listView.setAlternatingRowColors(True)
        newTab.listView.setSelectionMode(QAbstractItemView.MultiSelection)
        newTab.listView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        newTab.listView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        newTab.horizontalLayout.addWidget(newTab.listView)

        newTab.listModel = SqlTableModel(self.dbManager.connection, 'inventory', 'name', Qt.AscendingOrder, 'category=%s',
                                         (id,), ('name',))
        newTab.listView.setModel(newTab.listModel)
        newTab.listView.selectionModel().selectionChanged.connect(self.selectItem)

        # Add tab to tab widget as well as the tabDict variable
        self.categoryTabWidget.addTab(newTab.widget, name)
        self.tabDict[id] = newTab

    @pyqtSlot()
    def selectItem(self):
        hasSelection = not self.sender().selection().isEmpty()
        self.addBtn.setEnabled(hasSelection)
        self.removeBtn.setEnabled(hasSelection)

    @pyqtSlot(int)
    def on_categoryTabWidget_currentChanged(self, index):
        # If the index is zero, this get the selection model for the favorite's tab, otherwise, get the selection model
        # for the indexed tab.
        if index == 0:
            selectionModel = self.favoritesTableView.selectionModel()
        else:
            # Get category ID by looking up index in categories variable
            categoryID = self.categories[index - 1]['id']

            # Get selection model based on category ID
            selectionModel = self.tabDict[categoryID].listView.selectionModel()

        hasSelection = not selectionModel.selection().isEmpty()
        self.addBtn.setEnabled(hasSelection)
        self.removeBtn.setEnabled(hasSelection)

    @pyqtSlot()
    def showEvent(self, event):
        self.centralWindow.primaryScanner.barcodeReceived.connect(self.primaryScanner_barcodeReceived)
        self.centralWindow.secondaryScanner.barcodeReceived.connect(self.secondaryScanner_barcodeReceived)

    @pyqtSlot()
    def hideEvent(self, event):
        self.centralWindow.primaryScanner.barcodeReceived.disconnect(self.primaryScanner_barcodeReceived)
        self.centralWindow.secondaryScanner.barcodeReceived.disconnect(self.secondaryScanner_barcodeReceived)

    @pyqtSlot()
    def on_backBtn_clicked(self):
        self.parent().setCurrentIndex(WindowType.Main)

    @pyqtSlot()
    def on_homeBtn_clicked(self):
        self.parent().setCurrentIndex(WindowType.Main)

    @pyqtSlot()
    def on_listAddBtn_clicked(self):
        # Create a ManualAddDialog, pass the configuration variables such as config, dbManager and categories
        # The category combo box in the dialog will be set to the currently selected tab in the Favorite's Menu. However,
        # if the currently selected tab is the favorite's, then it will default to the first category
        dialog = ManualAddDialog(self.config, self.dbManager, self.categories,
                                 max(self.categoryTabWidget.currentIndex() - 1, 0), self)

        # Run the dialog, if successfully completed, then add new item to category
        if dialog.exec():
            item = {}

            catComboInd = dialog.categoryComboBox.currentIndex()
            item['name'] = dialog.nameEdit.text()
            item['category'] = dialog.categories[catComboInd]['id']

            if dialog.favoritesCheckbox.isChecked():
                index = self.dbManager.GetFavoritesCount()
                if index is None: # If the values are all NULL, set to 0
                    index = 0

                index += 1 # Increment index by 1
                item['favoritesIndex'] = index

            self.dbManager.AddItemToInventory(item)

            # If the category currently exists (check tabDict for the id), then refresh the list model by calling select
            # Otherwise, the category will be added later on and it will automatically be updated on creation
            if item['category'] in self.tabDict:
                self.tabDict[item['category']].listModel.select()

        # If the categories list that was sent to the dialog is not the same when finishing, that means a new category
        # was added and the new category list was queried. Update the categories variable in FavoriteWindow and add the
        # appropiate tabs
        if self.categories is not dialog.categories:
            self.categories = dialog.categories

            for category in self.categories:
                if not category['id'] in self.tabDict:
                    self.addTab(category['id'], category['name'])

    @pyqtSlot(str)
    def primaryScanner_barcodeReceived(self, barcode):
        print("Fav: Primary barcode scanner got: %s" % barcode)
        # TODO Send the barcode scanner information to be processed

    @pyqtSlot(str)
    def secondaryScanner_barcodeReceived(self, barcode):
        print("Fav: Secondary barcode scanner got: %s" % barcode)
        # TODO Send the barcode scanner information to be processed
