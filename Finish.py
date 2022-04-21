# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Finish.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Finish(object):
    def setupUi(self, Finish):
        Finish.setObjectName("Finish")
        Finish.resize(506, 309)
        Finish.setMinimumSize(QtCore.QSize(506, 309))
        self.label = QtWidgets.QLabel(Finish)
        self.label.setGeometry(QtCore.QRect(110, 40, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Finish)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 181, 31))
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
        self.label_3 = QtWidgets.QLabel(Finish)
        self.label_3.setGeometry(QtCore.QRect(120, 100, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Finish)
        self.label_4.setGeometry(QtCore.QRect(20, 250, 561, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Finish)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 561, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(7)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Finish)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(7)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.button_closeProject = QtWidgets.QPushButton(Finish)
        self.button_closeProject.setGeometry(QtCore.QRect(160, 140, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_closeProject.setFont(font)
        self.button_closeProject.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_closeProject.setObjectName("button_closeProject")

        self.retranslateUi(Finish)
        QtCore.QMetaObject.connectSlotsByName(Finish)

    def retranslateUi(self, Finish):
        _translate = QtCore.QCoreApplication.translate
        Finish.setWindowTitle(_translate("Finish", "CIDC Challenge"))
        self.label.setText(_translate("Finish", "Building a report trough a spread sheet"))
        self.label_2.setText(_translate("Finish", "CIDC Challenge"))
        self.label_3.setText(_translate("Finish", "Thank you for using our software."))
        self.label_4.setText(_translate("Finish", "Pedro Lopes de Oliveira - Undergraduated Telecommunications Engineer "))
        self.label_5.setText(_translate("Finish", "Yara Caroline Tavares Mendes - Undergraduated Telecommunications Engineer"))
        self.label_6.setText(_translate("Finish", "Developed by:"))
        self.button_closeProject.setText(_translate("Finish", "Close Project"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Finish = QtWidgets.QDialog()
    ui = Ui_Finish()
    ui.setupUi(Finish)
    Finish.show()
    sys.exit(app.exec_())
