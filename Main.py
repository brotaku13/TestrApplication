from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MainWindow import mainWindow
from MainWindow.LoginWindowPackage.LoginWindowClass import LoginWindow as login
import sys

def main():
    app = QApplication(sys.argv)
    loginWindow = login()
    testrInstance = mainWindow.TestrMainWindow()
    if loginWindow.exec_():  # uncomment to allow login window
        testrInstance.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()