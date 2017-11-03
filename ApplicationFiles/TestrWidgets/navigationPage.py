from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ApplicationFiles.TestrWidgets.NavigationPageWidgets.Account import Account
from ApplicationFiles.TestrWidgets.NavigationPageWidgets.QuestionBrowser import QuestionBrowser


class NavigationPage(QWidget):

    def __init__(self, parent=None):
        super(NavigationPage, self).__init__(parent)

        self.account = Account()
        self.questionBrowser = QuestionBrowser()
        self.defineLayout()


    def defineLayout(self):
        totalLayout = QVBoxLayout()
        totalLayout.addWidget(self.account)
        totalLayout.addWidget(self.questionBrowser)

        self.setLayout(totalLayout)


