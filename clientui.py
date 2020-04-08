# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messenger.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExampleMessenger(object):
    def setupUi(self, ExampleMessenger):
        ExampleMessenger.setObjectName("ExampleMessenger")
        ExampleMessenger.resize(462, 563)
        font = QtGui.QFont()
        font.setPointSize(24)
        ExampleMessenger.setFont(font)
        self.centralwidget = QtWidgets.QWidget(ExampleMessenger)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 90, 441, 381))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.message = QtWidgets.QTextEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(10, 480, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.message.setFont(font)
        self.message.setObjectName("message")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 480, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(70, 10, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 10, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(300, 10, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.create_user_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_user_button.setGeometry(QtCore.QRect(100, 40, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        self.create_user_button.setFont(font)
        self.create_user_button.setObjectName("create_user_button")
        ExampleMessenger.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ExampleMessenger)
        self.statusbar.setObjectName("statusbar")
        ExampleMessenger.setStatusBar(self.statusbar)

        self.retranslateUi(ExampleMessenger)
        QtCore.QMetaObject.connectSlotsByName(ExampleMessenger)

    def retranslateUi(self, ExampleMessenger):
        _translate = QtCore.QCoreApplication.translate
        ExampleMessenger.setWindowTitle(_translate("ExampleMessenger", "Example Messenger"))
        self.pushButton.setText(_translate("ExampleMessenger", "Send"))
        self.label_2.setText(_translate("ExampleMessenger", "Login"))
        self.label_3.setText(_translate("ExampleMessenger", "Password"))
        self.create_user_button.setText(_translate("ExampleMessenger", "New User"))
