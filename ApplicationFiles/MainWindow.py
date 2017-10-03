from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Testr.ApplicationFiles.TestrWidgets.CodingWindow import CodingWindow
import os
import sys

class mainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.resize(1300, 900)

        self.setWindowIcon(QIcon("C:\\Users\\Brian\\Documents\\school\\PythonProjects\\Testr\\ApplicationFiles\\Resources\\test_passed-512.png"))

        self.setWindowTitle("Testr")

        #sets central widget to a stacked widget
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.stack.setObjectName('stackedWidget')

        self.codingWindow = CodingWindow()
        self.stack.addWidget(self.codingWindow)

        #sets up statusbar and menubar, both are objects of the mainwindow, not of the widgets inside of it.
        self.mainWindowProperties()

    def mainWindowProperties(self):

        # setting up status bar
        self.questionStatus = QLabel()
        self.status = self.statusBar()
        self.status.setSizeGripEnabled(False)
        self.status.addPermanentWidget(self.questionStatus)
        self.status.showMessage("ready")

        #defining menubar
        self.defineMenuBarActions()

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
        #self.questionBrowserNavAction = self.createAction("Question Browser", self.index1_emit, "Crtl+2", "Navigate to Question Browser")

        #self.testPageNavAction = self.createAction("&Testing Page", self.index0_emit, "Ctrl+1", "Navigate to testing screen")

        #self.menuBar.addAction(self.testPageNavAction)
        #self.menuBar.addAction(self.questionBrowserNavAction)

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



