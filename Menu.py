# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Second_Window(object):

    def setupUi(self, Second_Window):
        Second_Window.setObjectName("Second_Window")
        Second_Window.resize(410, 400)
        Second_Window.setMinimumSize(QtCore.QSize(400, 300))
        Second_Window.setMaximumSize(QtCore.QSize(410, 400))
        self.label_2 = QtWidgets.QLabel(Second_Window)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 181, 31))
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
        self.button_operators = QtWidgets.QPushButton(Second_Window)
        self.button_operators.setGeometry(QtCore.QRect(70, 90, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_operators.setFont(font)
        self.button_operators.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_operators.setObjectName("button_operators")
        self.button_services = QtWidgets.QPushButton(Second_Window)
        self.button_services.setGeometry(QtCore.QRect(70, 140, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_services.setFont(font)
        self.button_services.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_services.setObjectName("button_services")
        self.button_employees = QtWidgets.QPushButton(Second_Window)
        self.button_employees.setGeometry(QtCore.QRect(70, 190, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_employees.setFont(font)
        self.button_employees.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_employees.setObjectName("button_employees")
        self.button_graphics = QtWidgets.QPushButton(Second_Window)
        self.button_graphics.setGeometry(QtCore.QRect(70, 240, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_graphics.setFont(font)
        self.button_graphics.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_graphics.setObjectName("button_graphics")
        self.button_close = QtWidgets.QPushButton(Second_Window)
        self.button_close.setGeometry(QtCore.QRect(70, 330, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_close.setFont(font)
        self.button_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_close.setObjectName("button_close")
        self.label = QtWidgets.QLabel(Second_Window)
        self.label.setGeometry(QtCore.QRect(60, 40, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Second_Window)
        QtCore.QMetaObject.connectSlotsByName(Second_Window)

    def retranslateUi(self, Second_Window):
        _translate = QtCore.QCoreApplication.translate
        Second_Window.setWindowTitle(_translate("Second_Window", "CIDC Challenge - Menu"))
        self.label_2.setText(_translate("Second_Window", "CIDC Challenge"))
        self.button_operators.setText(_translate("Second_Window", "Operators"))
        self.button_services.setText(_translate("Second_Window", "Services"))
        self.button_employees.setText(_translate("Second_Window", "Employees"))
        self.button_graphics.setText(_translate("Second_Window", "Graphics"))
        self.button_close.setText(_translate("Second_Window", "Close"))
        self.label.setText(_translate("Second_Window", "Building a report trough a spread sheet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Second_Window = QtWidgets.QDialog()
    ui = Ui_Second_Window()
    ui.setupUi(Second_Window)
    Second_Window.show()
    sys.exit(app.exec_())
