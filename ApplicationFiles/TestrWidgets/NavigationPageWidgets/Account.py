from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Account(QWidget):

    def __init__(self, parent=None):
        super(Account, self).__init__(parent)
        self.setMinimumHeight(450)