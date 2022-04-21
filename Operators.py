# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Operators.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Operators(object):
    def setupUi(self, Operators):
        Operators.setObjectName("Operators")
        Operators.resize(700, 500)
        Operators.setMinimumSize(QtCore.QSize(700, 500))
        Operators.setMaximumSize(QtCore.QSize(700, 500))
        self.label_2 = QtWidgets.QLabel(Operators)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 181, 31))
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
        self.label = QtWidgets.QLabel(Operators)
        self.label.setGeometry(QtCore.QRect(320, 40, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Operators)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Operators)
        self.label_4.setGeometry(QtCore.QRect(590, 60, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Operators)
        self.line.setGeometry(QtCore.QRect(340, 70, 20, 411))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.text_operators = QtWidgets.QTextBrowser(Operators)
        self.text_operators.setGeometry(QtCore.QRect(20, 80, 311, 371))
        self.text_operators.setObjectName("text_operators")
        self.text_woOperators = QtWidgets.QTextBrowser(Operators)
        self.text_woOperators.setGeometry(QtCore.QRect(370, 80, 311, 371))
        self.text_woOperators.setObjectName("text_woOperators")
        self.button_backOperators = QtWidgets.QPushButton(Operators)
        self.button_backOperators.setGeometry(QtCore.QRect(590, 460, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.button_backOperators.setFont(font)
        self.button_backOperators.setObjectName("button_backOperators")

        self.retranslateUi(Operators)
        QtCore.QMetaObject.connectSlotsByName(Operators)

    def retranslateUi(self, Operators):
        _translate = QtCore.QCoreApplication.translate
        Operators.setWindowTitle(_translate("Operators", "CIDC Challenge - Operators menu"))
        self.label_2.setText(_translate("Operators", "CIDC Challenge"))
        self.label.setText(_translate("Operators", "Operators"))
        self.label_3.setText(_translate("Operators", "With outliers"))
        self.label_4.setText(_translate("Operators", "Without outliers"))
        self.button_backOperators.setText(_translate("Operators", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Operators = QtWidgets.QDialog()
    ui = Ui_Operators()
    ui.setupUi(Operators)
    Operators.show()
    sys.exit(app.exec_())
