from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from .LoginPage import LoginPage
from .RegistrationPage import RegistrationPage
import os
import sys

class MainLoginWindow(QDialog):
    """Container class for the login window
    Inherits from QDialog class which is a standard popup window class. 
    """

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
        """Called when the information the user entered is correct and matches the information from the database. 
        Allows the user to login. Once this is called, the dialog window closes and the mainwindow is launched with the correct user information. 
        """
        self.accept()

    @pyqtSlot(int)
    def changePage(self, index):
        """Slot to change loginwindow page. flips between registration and the credential page. 
        
        Arguments:
            index {Int} -- the index of the page to be flipped to.
            index == 0 -> flips to login. 
            index = 1 -> flips to registration page. 
        """
        self.stack.setCurrentIndex(index)
        self.registrationPage.pictureFilePath.setText('')
