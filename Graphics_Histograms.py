# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Graphics_Histograms.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Histograms(object):
    def setupUi(self, Histograms):
        Histograms.setObjectName("Histograms")
        Histograms.resize(400, 272)
        Histograms.setMinimumSize(QtCore.QSize(400, 272))
        self.label = QtWidgets.QLabel(Histograms)
        self.label.setGeometry(QtCore.QRect(150, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Histograms)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 181, 31))
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
        self.button_histograms_CO = QtWidgets.QPushButton(Histograms)
        self.button_histograms_CO.setGeometry(QtCore.QRect(30, 100, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_histograms_CO.setFont(font)
        self.button_histograms_CO.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_histograms_CO.setObjectName("button_histograms_CO")
        self.button_histograms_DO = QtWidgets.QPushButton(Histograms)
        self.button_histograms_DO.setGeometry(QtCore.QRect(30, 150, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_histograms_DO.setFont(font)
        self.button_histograms_DO.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_histograms_DO.setObjectName("button_histograms_DO")
        self.button_backEmployees = QtWidgets.QPushButton(Histograms)
        self.button_backEmployees.setGeometry(QtCore.QRect(30, 200, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_backEmployees.setFont(font)
        self.button_backEmployees.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_backEmployees.setObjectName("button_backEmployees")

        self.retranslateUi(Histograms)
        QtCore.QMetaObject.connectSlotsByName(Histograms)

    def retranslateUi(self, Histograms):
        _translate = QtCore.QCoreApplication.translate
        Histograms.setWindowTitle(_translate("Histograms", "CIDC Challenge"))
        self.label.setText(_translate("Histograms", "Histograms"))
        self.label_2.setText(_translate("Histograms", "CIDC Challenge"))
        self.button_histograms_CO.setText(_translate("Histograms", "Considering Outliers"))
        self.button_histograms_DO.setText(_translate("Histograms", "Desconsidering Outliers"))
        self.button_backEmployees.setText(_translate("Histograms", "Back"))
