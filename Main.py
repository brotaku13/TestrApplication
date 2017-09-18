from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MainWindow import mainWindow
import sys

def main():
    app = QApplication(sys.argv)
    testrInstance = mainWindow.TestrMainWindow()
    testrInstance.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()