# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Graphics_Employees.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Graphics_Employees(object):
    def setupUi(self, Graphics_Employees):
        Graphics_Employees.setObjectName("Graphics_Employees")
        Graphics_Employees.resize(400, 238)
        Graphics_Employees.setMinimumSize(QtCore.QSize(400, 238))
        self.label_2 = QtWidgets.QLabel(Graphics_Employees)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Graphics_Employees)
        self.label.setGeometry(QtCore.QRect(150, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.button_meanEmployees = QtWidgets.QPushButton(Graphics_Employees)
        self.button_meanEmployees.setGeometry(QtCore.QRect(30, 100, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_meanEmployees.setFont(font)
        self.button_meanEmployees.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_meanEmployees.setObjectName("button_meanEmployees")
        self.button_backEmployees = QtWidgets.QPushButton(Graphics_Employees)
        self.button_backEmployees.setGeometry(QtCore.QRect(30, 150, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_backEmployees.setFont(font)
        self.button_backEmployees.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_backEmployees.setObjectName("button_backEmployees")

        self.retranslateUi(Graphics_Employees)
        QtCore.QMetaObject.connectSlotsByName(Graphics_Employees)

    def retranslateUi(self, Graphics_Employees):
        _translate = QtCore.QCoreApplication.translate
        Graphics_Employees.setWindowTitle(_translate("Graphics_Employees", "CIDC Challenge"))
        self.label_2.setText(_translate("Graphics_Employees", "CIDC Challenge"))
        self.label.setText(_translate("Graphics_Employees", "Employees"))
        self.button_meanEmployees.setText(_translate("Graphics_Employees", "Mean"))
        self.button_backEmployees.setText(_translate("Graphics_Employees", "Back"))
