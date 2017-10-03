from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Testr.ApplicationFiles.TestrWidgets.LoginWidgets.LoginPage import LoginPage
from Testr.ApplicationFiles.TestrWidgets.LoginWidgets.RegistrationPage import RegistrationPage
import os
import sys

class MainLoginWindow(QDialog):



    def __init__(self, parent=None):
        super(MainLoginWindow, self).__init__(parent)
        self.resize(500, 700)
        self.setWindowTitle("Login")

        self.stack = QStackedWidget()
        self.loginPage = LoginPage()
        self.stack.addWidget(self.loginPage)
        self.registrationPage = RegistrationPage()
        self.stack.addWidget(self.registrationPage)

        layout = QHBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

        self.loginPage.acceptSignal.connect(self.acceptDialog)
        self.registrationPage.pageIndexSignal.connect(self.changePage)
        self.loginPage.pageIndexSignal.connect(self.changePage)

    @pyqtSlot()
    def acceptDialog(self):
        print("emited successfully")
        self.accept()

    @pyqtSlot(int)
    def changePage(self, index):
        self.stack.setCurrentIndex(index)
