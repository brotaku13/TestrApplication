from PyQt5.QtWidgets import *
from ApplicationFiles.MainWindow import mainWindow
from ApplicationFiles.TestrWidgets.LoginWidgets.LoginWindow import MainLoginWindow as login
import sys

def main():
    app = QApplication(sys.argv)

    loginWindow = login()

    if loginWindow.exec_():
        testrInstance = mainWindow()
        testrInstance.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()