# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_Window(object):
    def setupUi(self, Main_Window):
        Main_Window.setObjectName("Main_Window")
        Main_Window.resize(512, 191)
        Main_Window.setMinimumSize(QtCore.QSize(512, 191))
        Main_Window.setMaximumSize(QtCore.QSize(512, 191))
        self.label_2 = QtWidgets.QLabel(Main_Window)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 181, 31))
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
        self.label = QtWidgets.QLabel(Main_Window)
        self.label.setGeometry(QtCore.QRect(50, 60, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.search = QtWidgets.QTextEdit(Main_Window)
        self.search.setGeometry(QtCore.QRect(50, 90, 231, 31))
        self.search.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.search.setObjectName("search")
        self.button_ok_mainMenu = QtWidgets.QPushButton(Main_Window)
        self.button_ok_mainMenu.setGeometry(QtCore.QRect(290, 90, 51, 31))
        self.button_ok_mainMenu.setMaximumSize(QtCore.QSize(16777207, 16777209))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.button_ok_mainMenu.setFont(font)
        self.button_ok_mainMenu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_ok_mainMenu.setAutoRepeatDelay(301)
        self.button_ok_mainMenu.setAutoRepeatInterval(101)
        self.button_ok_mainMenu.setObjectName("button_ok_mainMenu")
        self.label_3 = QtWidgets.QLabel(Main_Window)
        self.label_3.setGeometry(QtCore.QRect(100, 210, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Main_Window)
        self.label_4.setGeometry(QtCore.QRect(50, 130, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Main_Window)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

    def retranslateUi(self, Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("Main_Window", "CIDC Challenge - Search archive"))
        self.label_2.setText(_translate("Main_Window", "CIDC Challenge"))
        self.label.setText(_translate("Main_Window", "Archive name:"))
        self.button_ok_mainMenu.setText(_translate("Main_Window", "Ok"))
        self.label_3.setText(_translate("Main_Window", "(.xls)"))
        self.label_4.setText(_translate("Main_Window", "It should be without extension and a .xlsx"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_Window = QtWidgets.QDialog()
    ui = Ui_Main_Window()
    ui.setupUi(Main_Window)
    Main_Window.show()
    sys.exit(app.exec_())
