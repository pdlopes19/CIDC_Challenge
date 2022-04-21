# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Start.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_button_start(object):
    def setupUi(self, button_start):
        button_start.setObjectName("button_start")
        button_start.resize(559, 260)
        button_start.setMinimumSize(QtCore.QSize(559, 260))
        button_start.setMaximumSize(QtCore.QSize(559, 260))
        self.centralwidget = QtWidgets.QWidget(button_start)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 181, 31))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 50, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 561, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 190, 561, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(7)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.button_startProject = QtWidgets.QPushButton(self.centralwidget)
        self.button_startProject.setGeometry(QtCore.QRect(200, 100, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_startProject.setFont(font)
        self.button_startProject.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_startProject.setObjectName("button_startProject")
        button_start.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(button_start)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 559, 26))
        self.menubar.setObjectName("menubar")
        button_start.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(button_start)
        self.statusbar.setObjectName("statusbar")
        button_start.setStatusBar(self.statusbar)

        self.retranslateUi(button_start)
        QtCore.QMetaObject.connectSlotsByName(button_start)

    def retranslateUi(self, button_start):
        _translate = QtCore.QCoreApplication.translate
        button_start.setWindowTitle(_translate("button_start", "CIDC Challenge - Building a report trough a spread sheet"))
        self.label_2.setText(_translate("button_start", "CIDC Challenge"))
        self.label.setText(_translate("button_start", "Building a report trough a spread sheet"))
        self.label_3.setText(_translate("button_start", "Developed by:"))
        self.label_4.setText(_translate("button_start", "Pedro Lopes de Oliveira - Undergraduated Telecommunications Engineer "))
        self.label_5.setText(_translate("button_start", "Yara Caroline Tavares Mendes - Undergraduated Telecommunications Engineer"))
        self.button_startProject.setText(_translate("button_start", "Start Project"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    button_start = QtWidgets.QMainWindow()
    ui = Ui_button_start()
    ui.setupUi(button_start)
    button_start.show()
    sys.exit(app.exec_())
