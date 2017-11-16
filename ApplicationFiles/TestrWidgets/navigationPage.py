from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ApplicationFiles.TestrWidgets.NavigationPageWidgets.Account import Account
from ApplicationFiles.TestrWidgets.NavigationPageWidgets.QuestionBrowser import QuestionBrowser
import sys
import ApplicationFiles.Resources.SaveInfo as save


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

"""
app = QApplication(sys.argv)
form = NavigationPage()
form.show()
sys.exit(app.exec_())
"""



