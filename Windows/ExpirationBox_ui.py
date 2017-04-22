# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExpirationBox.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExpirationBox(object):
    def setupUi(self, ExpirationBox):
        ExpirationBox.setObjectName("ExpirationBox")
        ExpirationBox.resize(506, 364)
        font = QtGui.QFont()
        font.setPointSize(19)
        ExpirationBox.setFont(font)
        ExpirationBox.setStyleSheet("QDialog\n"
"{\n"
"    border: 1px solid #76797C;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(ExpirationBox)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.day_label = QtWidgets.QLabel(ExpirationBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.day_label.setFont(font)
        self.day_label.setAlignment(QtCore.Qt.AlignCenter)
        self.day_label.setObjectName("day_label")
        self.gridLayout.addWidget(self.day_label, 3, 2, 1, 1)
        self.day_combo = QtWidgets.QComboBox(ExpirationBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.day_combo.setFont(font)
        self.day_combo.setObjectName("day_combo")
        self.day_combo.addItem("")
        self.day_combo.setItemText(0, "")
        self.gridLayout.addWidget(self.day_combo, 4, 2, 1, 1)
        self.month_label = QtWidgets.QLabel(ExpirationBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.month_label.setFont(font)
        self.month_label.setAlignment(QtCore.Qt.AlignCenter)
        self.month_label.setObjectName("month_label")
        self.gridLayout.addWidget(self.month_label, 3, 1, 1, 1)
        self.month_combo = QtWidgets.QComboBox(ExpirationBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.month_combo.setFont(font)
        self.month_combo.setStyleSheet("QDialog\n"
"{\n"
"    border: 1px solid #76797C;\n"
"}")
        self.month_combo.setObjectName("month_combo")
        self.month_combo.addItem("")
        self.month_combo.setItemText(0, "")
        self.gridLayout.addWidget(self.month_combo, 4, 1, 1, 1)
        self.year_combo = QtWidgets.QComboBox(ExpirationBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.year_combo.setFont(font)
        self.year_combo.setObjectName("year_combo")
        self.year_combo.addItem("")
        self.year_combo.setItemText(0, "")
        self.gridLayout.addWidget(self.year_combo, 4, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 13, 1, 1, 1)
        self.year_label = QtWidgets.QLabel(ExpirationBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.year_label.setFont(font)
        self.year_label.setAlignment(QtCore.Qt.AlignCenter)
        self.year_label.setObjectName("year_label")
        self.gridLayout.addWidget(self.year_label, 3, 3, 1, 1)
        self.qty_label = QtWidgets.QLabel(ExpirationBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.qty_label.setFont(font)
        self.qty_label.setObjectName("qty_label")
        self.gridLayout.addWidget(self.qty_label, 6, 1, 1, 2)
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_1.setSpacing(15)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.cancel_label = QtWidgets.QLabel(ExpirationBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.cancel_label.setFont(font)
        self.cancel_label.setObjectName("cancel_label")
        self.horizontalLayout_1.addWidget(self.cancel_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_1.addItem(spacerItem1)
        self.accept_button = TouchButton(ExpirationBox)
        self.accept_button.setMinimumSize(QtCore.QSize(48, 48))
        self.accept_button.setMaximumSize(QtCore.QSize(48, 48))
        self.accept_button.setStyleSheet("background-color: transparent;\n"
"border: 0;")
        self.accept_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/GreenCheckIcon_Finished.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.accept_button.setIcon(icon)
        self.accept_button.setIconSize(QtCore.QSize(48, 48))
        self.accept_button.setObjectName("accept_button")
        self.horizontalLayout_1.addWidget(self.accept_button)
        self.cancel_button = TouchButton(ExpirationBox)
        self.cancel_button.setMinimumSize(QtCore.QSize(48, 48))
        self.cancel_button.setMaximumSize(QtCore.QSize(48, 48))
        self.cancel_button.setStyleSheet("background-color: transparent;\n"
"border: 0;")
        self.cancel_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/Icons/RedCancelIcon_Finished.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_button.setIcon(icon1)
        self.cancel_button.setIconSize(QtCore.QSize(48, 48))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_1.addWidget(self.cancel_button)
        self.gridLayout.addLayout(self.horizontalLayout_1, 14, 1, 1, 3)
        self.qty_combo = QtWidgets.QComboBox(ExpirationBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.qty_combo.setFont(font)
        self.qty_combo.setObjectName("qty_combo")
        self.gridLayout.addWidget(self.qty_combo, 7, 1, 1, 3)
        self.label = QtWidgets.QLabel(ExpirationBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.itemNameLabel = QtWidgets.QLabel(ExpirationBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.itemNameLabel.setFont(font)
        self.itemNameLabel.setObjectName("itemNameLabel")
        self.gridLayout.addWidget(self.itemNameLabel, 2, 2, 1, 2)
        self.exp_label = QtWidgets.QLabel(ExpirationBox)
        font = QtGui.QFont()
        font.setFamily("Cronus Round")
        font.setPointSize(21)
        self.exp_label.setFont(font)
        self.exp_label.setObjectName("exp_label")
        self.gridLayout.addWidget(self.exp_label, 1, 1, 1, 3, QtCore.Qt.AlignHCenter)

        self.retranslateUi(ExpirationBox)
        QtCore.QMetaObject.connectSlotsByName(ExpirationBox)

    def retranslateUi(self, ExpirationBox):
        _translate = QtCore.QCoreApplication.translate
        ExpirationBox.setWindowTitle(_translate("ExpirationBox", "Dialog"))
        self.day_label.setText(_translate("ExpirationBox", "Day"))
        self.month_label.setText(_translate("ExpirationBox", "Month"))
        self.year_label.setText(_translate("ExpirationBox", "Year"))
        self.qty_label.setText(_translate("ExpirationBox", "Quantity"))
        self.cancel_label.setText(_translate("ExpirationBox", "Scan to continue"))
        self.label.setText(_translate("ExpirationBox", "Item Name:"))
        self.itemNameLabel.setText(_translate("ExpirationBox", "Label"))
        self.exp_label.setText(_translate("ExpirationBox", "Expiration Date"))

from Widgets.touchButton import TouchButton
import Resource_BY_rc
import style_rc
