# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Graphics_Services.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Graphics_Services(object):
    def setupUi(self, Graphics_Services):
        Graphics_Services.setObjectName("Graphics_Services")
        Graphics_Services.resize(400, 300)
        Graphics_Services.setMinimumSize(QtCore.QSize(400, 300))
        self.label = QtWidgets.QLabel(Graphics_Services)
        self.label.setGeometry(QtCore.QRect(160, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Graphics_Services)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 181, 31))
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
        self.button_services_CO = QtWidgets.QPushButton(Graphics_Services)
        self.button_services_CO.setGeometry(QtCore.QRect(40, 100, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_services_CO.setFont(font)
        self.button_services_CO.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_services_CO.setObjectName("button_services_CO")
        self.button_services_DO = QtWidgets.QPushButton(Graphics_Services)
        self.button_services_DO.setGeometry(QtCore.QRect(40, 150, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_services_DO.setFont(font)
        self.button_services_DO.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_services_DO.setObjectName("button_services_DO")
        self.button_backOperators = QtWidgets.QPushButton(Graphics_Services)
        self.button_backOperators.setGeometry(QtCore.QRect(40, 230, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_backOperators.setFont(font)
        self.button_backOperators.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_backOperators.setObjectName("button_backOperators")

        self.retranslateUi(Graphics_Services)
        QtCore.QMetaObject.connectSlotsByName(Graphics_Services)

    def retranslateUi(self, Graphics_Services):
        _translate = QtCore.QCoreApplication.translate
        Graphics_Services.setWindowTitle(_translate("Graphics_Services", "CIDC Challenge"))
        self.label.setText(_translate("Graphics_Services", "Services"))
        self.label_2.setText(_translate("Graphics_Services", "CIDC Challenge"))
        self.button_services_CO.setText(_translate("Graphics_Services", "Unique Considering Outliers"))
        self.button_services_DO.setText(_translate("Graphics_Services", "Unique Desconsidering Outliers"))
        self.button_backOperators.setText(_translate("Graphics_Services", "Back"))
