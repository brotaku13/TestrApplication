from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import ApplicationFiles.Resources.filepaths as path
import ApplicationFiles.Resources.SaveInfo as save

class LoginPage(QWidget):
    """General Login Page. allows the user to enter in credentials and checks them against database pairs of username/passwords
    """
    acceptSignal = pyqtSignal()
    pageIndexSignal = pyqtSignal(int)

    def __init__(self, parent=None):
        super(LoginPage, self).__init__(parent)

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

        self.shortcut = QShortcut(QKeySequence("Return"), self)
        self.shortcut.activated.connect(self.loginCheck)


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

        self.setLayout(layout)



    def buttonBehavior(self):
        self.loginBtn.clicked.connect(self.loginCheck)
        self.newUserBtn.clicked.connect(self.emit_pageSignal_on_click)

    def emit_pageSignal_on_click(self):
        """Emits the page index when a button which changes the page is clicked. connects to the container widget. 
        """
        self.pageIndexSignal.emit(1)

    def loginCheck(self):
        """Checks credentials entered into the text fields against the text file in the given save path. 
        """
        try:
           f = open(path.loginCredentialsPath, 'r')
        except Exception as e:
            print(str(e))
        self.userName = self.userNameField.text()
        self.password = self.passwordField.text()

        accept = False
        for line in f:
            infoList = line.split(";")
            if infoList[0] == self.userName and infoList[1].rstrip() == self.password:
                f.close()
                accept = True
                break
        f.close()

        if accept:
            ## saves account information
            save.saveAccount(self.userName)

            self.acceptSignal.emit()

        else:
            self.showLoginError()
            self.userNameField.setFocus()

    def newUserSignUp(self):
        self.stack.setCurrentIndex(1)


    @pyqtSlot(int)
    def changePageIndex(self, index):
        self.stack.setCurrentIndex(index)


    def showLoginError(self):
        """Shows an error dialog box which pops up when the user enters the incorrect login credentials. 
        """
        errorMsg = QMessageBox()
        errorMsg.setIcon(QMessageBox.Warning)
        errorMsg.setWindowTitle("Username or password incorrect")
        errorMsg.setText("It appears that the username or password was incorrect, please re-enter your credentials")
        errorMsg.exec_()
