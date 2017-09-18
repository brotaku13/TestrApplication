from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MainWindow.SideBarWidget.StackedSideBar import Sidebar
import MainWindow.questionClassPackage.questionClass as qc

import sys


class TestrMainWindow(QMainWindow):

    changePageIndex = pyqtSignal(int)
    changeQuestionSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.resize(1300, 900)
        self.setStyleSheet("QTextEdit {font:12pt 'Consolas'}")

        #  used later as a container for all of the questions in the program
        self.questionList = qc.questionList
        print(qc.questionList)
        self.currentIndex = 0

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.stack.setObjectName('stackedWidget')

        # setting up status bar
        self.questionStatus = QLabel()
        self.status = self.statusBar()
        self.status.setSizeGripEnabled(False)
        self.status.addPermanentWidget(self.questionStatus)
        self.status.showMessage("ready")  # can add second argument for timing (milliseconds)

        #adding page to the stacked widget
        self.questionPage = QWidget()
        self.stack.addWidget(self.questionPage)
        self.questionBrowser = QWidget()
        self.stack.addWidget(self.questionBrowser)

        # problem title setup
        self.questionTitleLabel = QLabel(self.questionPage)
        self.questionTitleLabel.setText("Problem Title Goes Here")
        titleFont = QFont()
        titleFont.setPointSize(40)
        titleFont.setFamily("Trebuchet MS")
        self.questionTitleLabel.setFont(titleFont)
        self.questionTitleLabel.setAlignment(Qt.AlignBottom | Qt.AlignCenter)


        #previous and next buttons
        navButtonSizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.prevButton = QPushButton("<< Prev")
        self.prevButton.setObjectName("previousbutton")
        self.prevButton.setMaximumWidth(50)
        self.prevButton.setMaximumHeight(80)
        self.prevButton.setSizePolicy(navButtonSizePolicy)
        self.prevButton.clicked.connect(self.prevQuestion_emit)

        self.nextButton = QPushButton("Next >>")
        self.nextButton.setObjectName("nextbutton")
        self.nextButton.setMaximumWidth(50)
        self.nextButton.setMaximumHeight(80)
        self.nextButton.setSizePolicy(navButtonSizePolicy)
        self.nextButton.clicked.connect(self.nextQuestion_emit)


        # setting up textEdit
        self.textEdit = QTextEdit(self.questionPage)
        self.textEdit.setText("def functionName(): \n\tetc...")
        textEditFont = QFont()
        textEditFont.setFamily("Consolas")
        tabMetric = QFontMetrics(textEditFont)
        tabSpace = tabMetric.width("M" * 5)
        self.textEdit.setTabStopWidth(tabSpace)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)

        textEditSizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        textEditSizePolicy.setHorizontalStretch(0)
        textEditSizePolicy.setVerticalStretch(0)
        textEditSizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(textEditSizePolicy)
        self.textEdit.setMinimumSize(QSize(0, 0))

        """
        the following are used to instantiate multiple UI Factors
        """
        self.defineSideBar()
        self.defineLayout()
        self.defineMenuBarActions()
        self.defineSignalConnections()



        # basic update text fields function
        self.updateQuestionInformation()

    """
    place emits in this section
    """

    def index1_emit(self):
        self.changePageIndex.emit(1)

    def index0_emit(self):
        self.changePageIndex.emit(0)

    def prevQuestion_emit(self):
        self.changeQuestionSignal.emit("previousquestion")

    def nextQuestion_emit(self):
        self.changeQuestionSignal.emit("nextquestion")


    def userCode_emit(self):
        self.sidebar.userCode.emit(self.textEdit.toPlainText())

    """
    end emit section
    """


    def changePageIndexFunction(self, index):
        self.stack.setCurrentIndex(index)

    def changeQuesion(self, sender):

        questionListLen = len(self.questionList)
        if sender == "previousquestion":
            if self.currentIndex == 0:
                self.currentIndex = questionListLen - 1
            else:
                self.currentIndex -= 1
        elif sender == "nextquestion":
            self.currentIndex = (self.currentIndex + 1) % questionListLen
        self.updateQuestionInformation()




    """
    define any signals that need to be used
    """
    def defineSignalConnections(self):
        self.changePageIndex.connect(self.changePageIndexFunction)
        self.sidebar.userCode.connect(self.sidebar.on_run_code)
        self.changeQuestionSignal.connect(self.changeQuesion)




    """
    used to add Menu Actions to a menu easier
    """
    def addMenuItems(self, target, items):
        for item in items:
            if item is None:
                target.addSeparator()
            else:
                target.addAction(item)

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

    def defineMenuBarActions(self):

        # creating menu actions:
        quitAction = self.createAction("&Quit", self.close, "Ctrl+q", "Close the application", False)

        self.menuBar = self.menuBar()
        self.fileMenu = self.menuBar.addMenu("&File")
        self.fileMenu.addAction(quitAction)

        self.questionBrowserNavAction = self.createAction("Question Browser", self.index1_emit, "Crtl+2", "Navigate to Question Browser")
        #self.questionBrowserNavAction = QAction("Question Browser", self)
        #self.questionBrowserNavAction.triggered.connect(self.index1_emit)

        self.testPageNavAction = self.createAction("&Testing Page", self.index0_emit, "Ctrl+1", "Navigate to testing screen")
        #self.testPageNavAction = QAction("Testing Page", self)
        #self.testPageNavAction.triggered.connect(self.index0_emit)


        self.menuBar.addAction(self.testPageNavAction)
        self.menuBar.addAction(self.questionBrowserNavAction)

    def defineLayout(self):

        # layout shenanigans
        self.pageIndexNavLayout = QHBoxLayout()
        self.pageIndexNavLayout.addWidget(self.questionInfoButton)

        self.pageIndexNavLayout.addWidget(self.hintsAndHelpButton)

        self.informationSide = QVBoxLayout()
        self.informationSide.addLayout(self.pageIndexNavLayout)
        self.informationSide.addWidget(self.sidebar)
        self.informationSide.setSizeConstraint(QLayout.SetFixedSize)
        self.informationSide.setContentsMargins(0, -1, 0, -1)
        self.informationSide.setSpacing(0)

        self.codingSide = QVBoxLayout()
        self.navButtonLayout = QHBoxLayout()
        self.navButtonLayout.addWidget(self.prevButton)
        self.navButtonLayout.addWidget(self.questionTitleLabel)
        self.navButtonLayout.addWidget(self.nextButton)
        self.codingSide.addLayout(self.navButtonLayout)
        self.codingSide.addWidget(self.textEdit)
        self.codingSide.setContentsMargins(-1, -1, 0, -1)

        self.totalLayout = QHBoxLayout()
        self.totalLayout.addLayout(self.codingSide)
        self.totalLayout.addLayout(self.informationSide)

        self.questionPage.setLayout(self.totalLayout)


    def defineSideBar(self):
        self.sidebar = Sidebar()
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMaximumSize(QSize(450, 16777215))
        self.sidebar.runCodeButton.clicked.connect(self.userCode_emit)

        self.questionInfoButton = QPushButton("Question Information")
        self.questionInfoButton.setMinimumSize(QSize(100, 50))


        self.hintsAndHelpButton = QPushButton("Hints and Help")
        self.hintsAndHelpButton.setMinimumSize(QSize(100, 50))


    """
    updates text fields within the applications page
    """
    def updateQuestionInformation(self):

        self.questionTitleLabel.setText(qc.questionList[self.currentIndex].title)
        self.textEdit.setText(qc.questionList[self.currentIndex].initialFunction)
        self.sidebar.setQuestionInfo(qc.questionList[self.currentIndex].questionInformation)
        self.status.showMessage("You Switched to {}".format(qc.questionList[self.currentIndex].title), 3000)

        # initialize hints section here as well




