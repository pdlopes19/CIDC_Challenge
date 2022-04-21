# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Graphics.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.label_2 = QtWidgets.QLabel(Dialog)
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
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Graphics = QtWidgets.QLabel(Dialog)
        self.Graphics.setGeometry(QtCore.QRect(60, 50, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        self.Graphics.setFont(font)
        self.Graphics.setObjectName("Graphics")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(250, 50, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.graphic = QtWidgets.QGraphicsView(Dialog)
        self.graphic.setGeometry(QtCore.QRect(30, 70, 141, 181))
        self.graphic.setObjectName("graphic")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(190, 60, 20, 201))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.graphic_wo = QtWidgets.QGraphicsView(Dialog)
        self.graphic_wo.setGeometry(QtCore.QRect(230, 70, 141, 181))
        self.graphic_wo.setObjectName("graphic_wo")
        self.button_graphics = QtWidgets.QPushButton(Dialog)
        self.button_graphics.setGeometry(QtCore.QRect(290, 260, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.button_graphics.setFont(font)
        self.button_graphics.setObjectName("button_graphics")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CIDC Challenge - Graphics menu"))
        self.label_2.setText(_translate("Dialog", "CIDC Challenge"))
        self.label.setText(_translate("Dialog", "Graphics:"))
        self.Graphics.setText(_translate("Dialog", "With outliers"))
        self.label_4.setText(_translate("Dialog", "Without outliers"))
        self.button_graphics.setText(_translate("Dialog", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
