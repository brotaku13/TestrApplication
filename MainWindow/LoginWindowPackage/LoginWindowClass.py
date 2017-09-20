from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MainWindow.LoginWindowPackage.signupPage import SignupPage
import os
import sys


class LoginWindow(QDialog):
    resource_path = "C:\\Users\\brian\\Documents\\Programming\\Python\\python projects\\TestrApplication\\MainWindow\\Resources\\userInformation"
    resource_path = os.path.join(resource_path, "loginInformation.txt")

    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.resize(500, 700)
        self.setWindowTitle("Login")


        self.stack = QStackedWidget(self)
        self.loginPage = QWidget()
        self.signupPage = SignupPage()
        self.stack.addWidget(self.loginPage)
        self.stack.addWidget(self.signupPage)

        self.userNameField = QLineEdit()
        self.userNameField.setMaximumWidth(300)

        self.userNameLabel = QLabel("Username")
        self.userNameLabel.setAlignment(Qt.AlignCenter)

        self.passwordField = QLineEdit()
        self.passwordField.setMaximumWidth(300)
        self.passwordField.setEchoMode(QLineEdit.Password)

        self.passwordLabel = QLabel("Password")
        self.passwordLabel.setAlignment(Qt.AlignCenter)

        self.loginBtn = QPushButton("Login")
        self.loginBtn.setMaximumWidth(200)

        self.newUserBtn = QPushButton("New User? Sign Up")
        self.newUserBtn.setMaximumWidth(200)

        self.buttonBehavior()
        self.defineLayout()



    def defineLayout(self):
        layout = QVBoxLayout()

        verticalSpacer1 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(verticalSpacer1)

        loginVerticalLayout = QVBoxLayout()
        loginVerticalLayout.addWidget(self.userNameField)
        loginVerticalLayout.addWidget(self.userNameLabel)
        loginHorizontalLayout = QHBoxLayout()
        loginHorizontalLayout.addLayout(loginVerticalLayout)
        layout.addLayout(loginHorizontalLayout)

        verticalSpacer2 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Preferred)
        layout.addItem(verticalSpacer2)

        passwordVerticalLayout = QVBoxLayout()
        passwordVerticalLayout.addWidget(self.passwordField)
        passwordVerticalLayout.addWidget(self.passwordLabel)
        passwordHorizontalLayout = QHBoxLayout()
        passwordHorizontalLayout.addLayout(passwordVerticalLayout)
        layout.addLayout(passwordHorizontalLayout)

        verticalSpacer3 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred)
        layout.addItem(verticalSpacer3)

        buttonVerticalLayout = QVBoxLayout()
        buttonVerticalLayout.addWidget(self.loginBtn)
        buttonVerticalLayout.addWidget(self.newUserBtn)
        buttonHorizontalLayout = QHBoxLayout()
        buttonHorizontalLayout.addLayout(buttonVerticalLayout)
        layout.addLayout(buttonHorizontalLayout)

        verticalSpacer4 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred)

        layout.addItem(verticalSpacer4)

        self.loginPage.setLayout(layout)
        totalPageLayout = QHBoxLayout()

        totalPageLayout.addWidget(self.stack)

        self.setLayout(totalPageLayout)




    def buttonBehavior(self):
        self.loginBtn.clicked.connect(self.loginCheck)
        self.newUserBtn.clicked.connect(self.newUserSignUp)

    def loginCheck(self):

        f = open(self.resource_path, 'r')

        self.userName = self.userNameField.text()
        self.password = self.passwordField.text()

        accept = False
        for line in f:
            infoList = line.split(";")
            if infoList[0] == self.userName and infoList[1] == self.password:
                f.close()
                accept = True
                break
        f.close()

        if accept:
            self.accept()
        else:

            self.showLoginError()
            self.userNameField.setFocus()

    def newUserSignUp(self):

        self.stack.setCurrentIndex(1)


    def showLoginError(self):
        errorMsg = QMessageBox()
        errorMsg.setIcon(QMessageBox.Warning)
        errorMsg.setWindowTitle("Username or password incorrect")
        errorMsg.setText("It appears that the username or password was incorrect, please re-enter your credentials")
        errorMsg.exec_()


"""
app = QApplication(sys.argv)
loginWindow = LoginWindow()
loginWindow.show()
sys.exit(app.exec_())
"""




