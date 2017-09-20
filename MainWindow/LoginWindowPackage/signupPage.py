from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import sys

class SignupPage(QWidget):

    def __init__(self, parent=None):
        super(SignupPage, self).__init__(parent)


        self.nameLabel = QLabel("Name")


        nameFont = QFont()

        self.firstNameField = QLineEdit()
        self.firstNameLabel = QLabel("First")
        self.firstNameLabel.setAlignment(Qt.AlignTop)

        self.lastNameField = QLineEdit()
        self.lastNameLabel = QLabel("Last")
        self.lastNameLabel.setAlignment(Qt.AlignTop)

        self.emailLabel = QLabel("Email")
        self.emailField = QLineEdit()

        self.userNameLabel = QLabel("Username")
        self.userNameField = QLineEdit()

        self.passwordLabel = QLabel("Password")
        self.passwordField = QLineEdit()

        self.regiserBtn = QPushButton("Register")
        self.cancelBtn = QPushButton("Cancel")

        #self.defineButtonClick()
        self.defineLayout()

    """
    defines layout
    """
    def defineLayout(self):
        form = QGridLayout()
        form.addWidget(self.nameLabel, 0, 0)
        form.addWidget(self.firstNameField, 1, 0)
        form.addWidget(self.lastNameField, 1, 1)
        form.addWidget(self.firstNameLabel, 2, 0)
        form.addWidget(self.lastNameLabel, 2, 1)
        form.addWidget(self.emailLabel, 3, 0)
        form.addWidget(self.emailField, 4, 0, 1, 2)
        form.addWidget(self.userNameLabel, 5, 0)
        form.addWidget(self.userNameField, 6, 0, 1, 2)
        form.addWidget(self.passwordLabel, 7, 0)
        form.addWidget(self.passwordField, 8, 0, 1, 2)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.regiserBtn)
        buttonLayout.addWidget(self.cancelBtn)

        totalFormLayout = QVBoxLayout()
        vspacer1 = QSpacerItem(20, 100, QSizePolicy.Expanding, QSizePolicy.Preferred)
        totalFormLayout.addItem(vspacer1)

        totalFormLayout.addLayout(form)
        vspacer2 = QSpacerItem(20, 100, QSizePolicy.Expanding, QSizePolicy.Preferred)
        totalFormLayout.addItem(vspacer2)
        totalFormLayout.addLayout(buttonLayout)

        self.setLayout(totalFormLayout)


    """
    defines button clicks
    """
    def defineButtonClick(self):
        self.regiserBtn.clicked.connect(self.registerUser())
        self.cancelBtn.clicked.connect()


    """
    function which retrieves information from user and stores in variables
    calls the function to store variables in SQL
    """
    def registerUser(self):
        self.firstName = self.firstNameField.text()
        self.lastName = self.lastNameField.text()
        self.email = self.emailField.text()
        self.username = self.userNameField.text()
        self.password = self.passwordField.text()

        #calls the function to store variables in the SQL database
        self.storeinSQL()
        #should return user to login page after information is stored

    def storeInSQL(self):
        return


