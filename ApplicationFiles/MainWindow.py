from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ApplicationFiles.TestrWidgets.CodingWindow import CodingWindow
import ApplicationFiles.Resources.filepaths as path
from ApplicationFiles.TestrWidgets.navigationPage import NavigationPage
from ApplicationFiles.TestrWidgets.GlossaryWidgets.Definitions import Definitions
import ApplicationFiles.Resources.QuestionClass as qc

import os
import sys
from ApplicationFiles.about import *


class mainWindow(QMainWindow):
    """The mainwindow container class for the Testr Widgets
    """
    changePageSignal = pyqtSignal(int)

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.resize(1300, 900)

        self.setWindowIcon(QIcon(path.mainWindowIcon))

        self.setWindowTitle("Testr")

        #sets central widget to a stacked widget
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.stack.setObjectName('stackedWidget')

        self.navigationPage = NavigationPage()
        self.stack.addWidget(self.navigationPage)  # navigationPage is index 0

        self.codingWindow = CodingWindow()
        self.stack.addWidget(self.codingWindow)  # coding Window is index 1

        self.glossary = Definitions()   # Defintions should be index 2
        self.stack.addWidget(self.glossary)

        self.mainWindowProperties()

        self.changePageSignal.connect(self.changePageIndexSlot)

        self.navigationPage.questionBrowser.questionSelectedSignal.connect(self.changeQuestionIndexSlot)
        self.navigationPage.questionBrowser.changePageSignal.connect(self.changePageIndexSlot)

        self.codingWindow.updateReportRows.connect(self.codingWindow.sidebar.questionInformationTab.updateReportRows)
        self.codingWindow.updateShowAnswer.connect(self.codingWindow.sidebar.hintsAndHelpTab.stateCheck)

        self.codingWindow.sidebar.hintsAndHelpTab.changeToGlossary.connect(self.changePageIndexSlot)

        self.codingWindow.sidebar.updateAccountInformation.connect(self.navigationPage.account.callUpdateTable)
        self.codingWindow.sidebar.updateProblemsSolved.connect(self.navigationPage.account.updateQuestionsSolved)

    def mainWindowProperties(self):
        """special function to set up the status bar located at the bottom of the page. 
        """

        # setting up status bar
        self.questionStatus = QLabel()
        self.status = self.statusBar()
        self.status.setSizeGripEnabled(False)
        self.status.addPermanentWidget(self.questionStatus)
        self.status.showMessage("ready")

        #defining menubar
        self.defineMenuBarActions()

    def changePageEmit(self):
        """Emitting signals based on object name. 
        Responsible for changing the page of the stacked widget and allowing the user to navigate through different pages
        """
        if self.sender().objectName() == "questionbrowsernavaction":
            self.changePageSignal.emit(0)
        elif self.sender().objectName() == "codingpage":
            self.changePageSignal.emit(1)
        elif self.sender().objectName() == "glossarypage":
            self.changePageSignal.emit(2)


    @pyqtSlot(int)
    def changePageIndexSlot(self, index):
        """catchs the change page signal and changes the stacked widget's current index
        
        Arguments:
            index {int} -- the index of the page to change to. 
        """
        self.stack.setCurrentIndex(index)

    @pyqtSlot(int)
    def changeQuestionIndexSlot(self, index):
        """Changes the current question index. 
        """
        self.codingWindow.updateQuestionInformation()

    def createAction(self, text, slot=None, shortcut=None, tip=None, checkable=False, signal="triggered"):
        """Factory Method for creating menu bar buttons. 
        """
        action = QAction(text, self)
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            getattr(action, signal).connect(slot)
        if checkable:
            action.setCheckable(True)
        return action

    def defineMenuBarActions(self):
        """Defining the menu bar actions and giving them trigger actions. 
        """
        self.about = About

        quitAction = self.createAction("&Quit", self.close, "Ctrl+q", "Close the application", False)
        aboutAction = self.createAction("&About", self.about, "Ctrl+a", "Pops about", False)

        self.menuBar = self.menuBar()
        self.fileMenu = self.menuBar.addMenu("&File")
        self.fileMenu.addAction(quitAction)
        self.fileMenu.addAction(aboutAction)

        self.questionBrowserNavAction = self.createAction("Account", self.changePageEmit, "Crtl+2", "Navigate to Question Browser")
        self.questionBrowserNavAction.setObjectName("questionbrowsernavaction")


        self.questionPage = self.createAction("&Testing Page", self.changePageEmit, "Ctrl+1", "Navigate to testing screen")
        self.questionPage.setObjectName("codingpage")

        self.glossaryPage = self.createAction("&Glossary", self.changePageEmit, "Ctrl+3", "Navigate to Glossary")
        self.glossaryPage.setObjectName("glossarypage")

        self.menuBar.addAction(self.questionPage)
        self.menuBar.addAction(self.questionBrowserNavAction)
        self.menuBar.addAction(self.glossaryPage)