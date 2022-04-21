# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Employees.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Employees(object):
    def setupUi(self, Employees):
        Employees.setObjectName("Employees")
        Employees.resize(700, 500)
        Employees.setMinimumSize(QtCore.QSize(700, 500))
        Employees.setMaximumSize(QtCore.QSize(700, 500))
        self.Graphics = QtWidgets.QLabel(Employees)
        self.Graphics.setGeometry(QtCore.QRect(270, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Graphics.setFont(font)
        self.Graphics.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Graphics.setObjectName("Graphics")
        self.label = QtWidgets.QLabel(Employees)
        self.label.setGeometry(QtCore.QRect(320, 40, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Employees)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Employees)
        self.label_4.setGeometry(QtCore.QRect(590, 60, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Employees)
        self.line.setGeometry(QtCore.QRect(340, 70, 20, 411))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.text_employees = QtWidgets.QTextBrowser(Employees)
        self.text_employees.setGeometry(QtCore.QRect(20, 80, 311, 371))
        self.text_employees.setObjectName("text_employees")
        self.text_woEmployees = QtWidgets.QTextBrowser(Employees)
        self.text_woEmployees.setGeometry(QtCore.QRect(370, 80, 311, 371))
        self.text_woEmployees.setObjectName("text_woEmployees")
        self.button_employees = QtWidgets.QPushButton(Employees)
        self.button_employees.setGeometry(QtCore.QRect(590, 460, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.button_employees.setFont(font)
        self.button_employees.setObjectName("button_employees")

        self.retranslateUi(Employees)
        QtCore.QMetaObject.connectSlotsByName(Employees)

    def retranslateUi(self, Employees):
        _translate = QtCore.QCoreApplication.translate
        Employees.setWindowTitle(_translate("Employees", "CIDC Challenge - Employees menu"))
        self.Graphics.setText(_translate("Employees", "CIDC Challenge"))
        self.label.setText(_translate("Employees", "Employees"))
        self.label_3.setText(_translate("Employees", "With outliers"))
        self.label_4.setText(_translate("Employees", "Without outliers"))
        self.button_employees.setText(_translate("Employees", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Employees = QtWidgets.QDialog()
    ui = Ui_Employees()
    ui.setupUi(Employees)
    Employees.show()
    sys.exit(app.exec_())
