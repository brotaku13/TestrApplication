from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import sys

class SignupPage(QWidget):


    pageIndexSignal = pyqtSignal(int)

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

        self.defineButtonClick()
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
        self.regiserBtn.clicked.connect(self.registerUser)
        self.cancelBtn.clicked.connect(self.emit_pageSignal_on_click)

    def emit_pageSignal_on_click(self):
        print("emits 0")
        self.pageIndexSignal.emit(0)


    """
    function which retrieves information from user and stores in variables
    calls the function to store variables in SQL
    """
    def registerUser(self):
        # this function needs to do the error checking too! dont forget!

        self.firstName = self.firstNameField.text()
        self.lastName = self.lastNameField.text()
        self.email = self.emailField.text()
        self.username = self.userNameField.text()
        self.password = self.passwordField.text()

        if self.legit_email(self.email) and self.legit_name(self.firstName) and self.legit_name(self.lastName) and self.legit_password(self.password) and self.legit_username(self.username):
            self.firstName = self.firstName.title()
            self.lastName = self.lastName.title()
            self.storeInSQL()
        else:
            #make a QDialog

        #calls the function to store variables in the SQL database
        #self.storeinSQL()

        #should return user to login page after information is stored
        #change page index here

    def storeInSQL(self):
        return


    def legit_email(self, email: str) -> bool:
        '''checks user-inputted email and returns a
        boolean based on if it was a good email
        returns T/F depnding if its good
        '''
        if len(email) == 0:
            print('You must enter an email!')
            return False

        if '@' not in email:
            print('Sorry, you need an "@" in your email.')
            return False

        if email[-4::] != '.com':
            print('Hey, you need to have a ".com"\
     at the end of your email')
            return False

        return True

    def legit_name(self, name: str) -> bool:
        '''checks both first and last names to see if they're legit
            has to be at least 2 letters, no special symbols
            function returns T/F depending if its good
        '''

        legit_letters = 'abcdefghijklmnopqrstuvwxyz'
        if len(name) <= 1:
            print('We discriminate against people with one\
     letter or non-existant names')
            print('Just kidding! Try again! Type in a real name!')
            return False

        for letter in name:
            if letter not in legit_letters:
                print("Please only use actual letters for your name.")
                return False

        return True

    def legit_username(self, username: str) -> bool:
        legit_characters = '0123456789_abcdefghijklmnopqrstuvwxyz.'

        if len(username) < 5:
            print('Your username should be at least 5 characters.')
            return False

        for letter in username:
            if letter not in legit_characters:
                print('You can only use numbers, letters and a "." and a "_"')
                return False
        return True

    def legit_password(self, password: str) -> bool:
        if len(password) < 6:
            print('Your password should be at least 6 letters!')
            return False

        if ' ' in password:
            print('You cannot have consecutive spaces in your password!')
            return False
        return True


