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

        self.firstName = self.firstName.title()
        self.lastName = self.lastName.title()


        try:
            self.legit_name(self.firstName)
            self.legit_name(self.lastName)
            self.legit_email(self.email)
            self.legit_username(self.username)
            self.legit_password(self.password)
        except name_exception as e:
            self.showRegisterError("Name Error", e)
        except email_exception as e:
            self.showRegisterError("Email Error", e)
        except username_Exception as e:
            self.showRegisterError("Username Error", e)
        except Exception as e:
            self.showRegisterError("Password Error", e)


        # calls the function to store variables in the SQL database
        # self.storeinSQL()

        # should return user to login page after information is stored
        # change page index here

    def storeInSQL(self):
        return

    def check(self):

        return False


    def legit_email(self, email: str) -> bool:
        '''checks user-inputted email and returns a
        boolean based on if it was a good email
        returns T/F depnding if its good
        '''
        if len(email) < 7:
            raise email_exception("not an email of appropriate length")

        elif '@' not in email:
            raise email_exception("No @ found in email")

        elif email[-4::] != '.com':
            raise email_exception("no .com found in email")


    def legit_name(self, name: str) -> bool:
        '''checks both first and last names to see if they're legit
            has to be at least 2 letters, no special symbols
            function returns T/F depending if its good
        '''
        if len(name) <= 1:
            raise name_exception("Name length must be more than 1")

        if not name.isalpha():
            raise name_exception("only letters are allowed in name")

    def legit_username(self, username: str) -> bool:
        legit_characters = '0123456789_abcdefghijklmnopqrstuvwxyz.'

        if len(username) < 5:
            raise username_Exception("Username must be more than 5 characters")

        for letter in username:
            if letter not in legit_characters:
                raise username_Exception("Illegal character found in username")

    def legit_password(self, password: str) -> bool:
        if len(password) < 6:
            raise password_exception("Password must be longer than 6 characters")

        if ' ' in password:
            raise password_exception("Cannot have spaces in password")


    def showRegisterError(self, title, e):
        errorMsg = QMessageBox()
        errorMsg.setIcon(QMessageBox.Warning)
        errorMsg.setWindowTitle(title)
        errorMsg.setText(str(e))
        errorMsg.exec_()


class email_exception(Exception):
    pass

class name_exception(Exception):
    pass

class password_exception(Exception):
    pass

class username_Exception(Exception):
    pass


