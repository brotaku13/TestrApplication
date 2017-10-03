from PyQt5.QtWidgets import *
from Testr.ApplicationFiles.MainWindow import mainWindow
from Testr.ApplicationFiles.TestrWidgets.LoginWidgets.LoginWindow import MainLoginWindow as login
import sys

def main():
    app = QApplication(sys.argv)
    testrInstance = mainWindow()
    loginWindow = login()
    if loginWindow.exec_():
        testrInstance.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()