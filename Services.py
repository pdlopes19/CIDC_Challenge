# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Services.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Services(object):
    def setupUi(self, Services):
        Services.setObjectName("Services")
        Services.resize(700, 500)
        Services.setMinimumSize(QtCore.QSize(700, 500))
        Services.setMaximumSize(QtCore.QSize(700, 500))
        self.label_2 = QtWidgets.QLabel(Services)
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
        self.label = QtWidgets.QLabel(Services)
        self.label.setGeometry(QtCore.QRect(320, 40, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Services)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Services)
        self.label_4.setGeometry(QtCore.QRect(590, 60, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.text_services = QtWidgets.QTextBrowser(Services)
        self.text_services.setGeometry(QtCore.QRect(20, 80, 311, 371))
        self.text_services.setObjectName("text_services")
        self.line = QtWidgets.QFrame(Services)
        self.line.setGeometry(QtCore.QRect(340, 70, 20, 411))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.text_woServices = QtWidgets.QTextBrowser(Services)
        self.text_woServices.setGeometry(QtCore.QRect(370, 80, 311, 371))
        self.text_woServices.setObjectName("text_woServices")
        self.button_services = QtWidgets.QPushButton(Services)
        self.button_services.setGeometry(QtCore.QRect(590, 460, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.button_services.setFont(font)
        self.button_services.setObjectName("button_services")

        self.retranslateUi(Services)
        QtCore.QMetaObject.connectSlotsByName(Services)

    def retranslateUi(self, Services):
        _translate = QtCore.QCoreApplication.translate
        Services.setWindowTitle(_translate("Services", "CIDC Challenge - Services menu"))
        self.label_2.setText(_translate("Services", "CIDC Challenge"))
        self.label.setText(_translate("Services", "Services"))
        self.label_3.setText(_translate("Services", "With outliers"))
        self.label_4.setText(_translate("Services", "Without outliers"))
        self.button_services.setText(_translate("Services", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Services = QtWidgets.QDialog()
    ui = Ui_Services()
    ui.setupUi(Services)
    Services.show()
    sys.exit(app.exec_())
