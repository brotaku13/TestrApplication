from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ApplicationFiles.TestrWidgets.CodingWindow import CodingWindow
import ApplicationFiles.Resources.filepaths as path
from ApplicationFiles.TestrWidgets.navigationPage import NavigationPage
import os
import sys

class mainWindow(QMainWindow):

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

        self.codingWindow = CodingWindow()
        self.stack.addWidget(self.codingWindow)

        self.navigationPage = NavigationPage()
        self.stack.addWidget(self.navigationPage)

        self.mainWindowProperties()
        #self.defineStyleSheets()
        #connect function for changing the page index
        self.changePageSignal.connect(self.changePageIndexSlot)


    def mainWindowProperties(self):

        # setting up status bar
        self.questionStatus = QLabel()
        self.status = self.statusBar()
        self.status.setSizeGripEnabled(False)
        self.status.addPermanentWidget(self.questionStatus)
        self.status.showMessage("ready")

        #defining menubar
        self.defineMenuBarActions()

    def changePageEmit(self):
        if self.sender().objectName() == "questionbrowsernavaction":
            self.changePageSignal.emit(1)
        elif self.sender().objectName() == "questionpage":
            self.changePageSignal.emit(0)

    @pyqtSlot(int)
    def changePageIndexSlot(self, index):
        self.stack.setCurrentIndex(index)

    """
    factory method for creating an action...used in menubar creation
    """

    def createAction(self, text, slot=None, shortcut=None, tip=None, checkable=False, signal="triggered"):
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


    """
    function defines any actions or buttons / shortcuts in the menubar.
    add all menu bar functionality here
    """
    def defineMenuBarActions(self):

        # creating menu actions:
        quitAction = self.createAction("&Quit", self.close, "Ctrl+q", "Close the application", False)

        self.menuBar = self.menuBar()
        self.fileMenu = self.menuBar.addMenu("&File")
        self.fileMenu.addAction(quitAction)

        """
        todo: create menubar actions
        """
        self.questionBrowserNavAction = self.createAction("Question Browser", self.changePageEmit, "Crtl+2", "Navigate to Question Browser")
        self.questionBrowserNavAction.setObjectName("questionbrowsernavaction")
        self.questionPage = self.createAction("&Testing Page", self.changePageEmit, "Ctrl+1", "Navigate to testing screen")
        self.questionPage.setObjectName("questionpage")
        self.menuBar.addAction(self.questionPage)
        self.menuBar.addAction(self.questionBrowserNavAction)

    def defineStyleSheets(self):
        self.setStyleSheet("""
           QCentralWidget {
               background-color:rgb(63, 63, 63);
           }
           QStackedWidget {
               background-color:rgb(63, 63, 63);
               color:rgb(26, 198, 26);
               selection-color:rgb(0,0,0);
               selection-background-color:rgb(26, 198, 26);
               font-family: "Ariel";

           }
           QTextEdit {
               background-color:rgb(44, 45, 44);
               color:rgb(26, 198, 26);
               selection-color:rgb(0,0,0);
               selection-background-color:rgb(26, 198, 26);
               font-family: "Consolas";
               font-size: 10pt;
               border:0px;
           }
           QLabel {
               color:rgb(26, 198, 26);
               selection-color:rgb(0,0,0);
               selection-background-color:rgb(26, 198, 26);
           }

           QPushButton {
               background-color:black;
               color:rgb(26, 198, 26);
               border-radius:10px;
           }
           QMenuBar{
               background-color:black;
               color:rgb(26, 198, 26);
           }
           """)



