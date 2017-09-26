from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MainWindow.SideBarWidget.StackedSideBar import Sidebar
import MainWindow.questionClassPackage.questionClass as qc
import os
import sys


class TestrMainWindow(QMainWindow):

    icon_path = os.path.dirname("C:\\Users\\brian\\Documents\\Programming\\Python\\python projects\\TestrApplication\\MainWindow\\Resources")
    icon_path = os.path.join(icon_path, "checklist.png")

    """
    setting up any pyqtSignals needed
    """
    changePageIndex = pyqtSignal(int)  # a signal that emits the page index we are on in the main StackedWidger
    changeQuestionSignal = pyqtSignal(int)  # signal which emits which button was pressed "previous/next"
    sidebarIndexSignal = pyqtSignal(int)

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.resize(1300, 900)

        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'test_passed-512')))
        self.setWindowTitle("Testr")


        #  used later as a container for all of the questions in the program
        self.questionList = qc.questionList
        self.currentQuestionIndex = 0  # current index of the mainStacked widget self.stack

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
        self.prevButton.setMaximumWidth(80)
        self.prevButton.setMaximumHeight(80)
        self.prevButton.setSizePolicy(navButtonSizePolicy)
        self.prevButton.clicked.connect(self.changeQuestionIndex)

        self.nextButton = QPushButton("Next >>")
        self.nextButton.setObjectName("nextbutton")
        self.nextButton.setMaximumWidth(80)
        self.nextButton.setMaximumHeight(80)
        self.nextButton.setSizePolicy(navButtonSizePolicy)
        self.nextButton.clicked.connect(self.changeQuestionIndex)


        # setting up textEdit
        self.textEdit = QTextEdit(self.questionPage)
        self.textEdit.setText("def functionName(): \n\tetc...")
        textEditFont = QFont()
        textEditFont.setFamily("Consolas")
        textEditFont.setStyleHint(QFont.Monospace)
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
        #self.defineStyleSheets()

        # basic update text fields function
        self.updateQuestionInformation()

    """
    emits the changePageIndex signal
    :returns switch to page index 0
    """
    def index1_emit(self):
        self.changePageIndex.emit(1)

    """
    emits the changePageIndex signal
    :returns switch to page index 1
    """
    def index0_emit(self):
        self.changePageIndex.emit(0)


    def userCode_emit(self):
        self.sidebar.userCode.emit(self.textEdit.toPlainText())


    def sidebar_index_emit(self):
        sender = self.sender()

        if sender.objectName() == "hintsandhelpbutton":

            self.sidebarIndexSignal.emit(1)
        else:

            self.sidebarIndexSignal.emit(0)


    """
    changes current main Stacked Widget index
    :param the index to set the page to
    """
    def changePageIndexFunction(self, index):
        self.stack.setCurrentIndex(index)


    @pyqtSlot(int)
    def setSideBarIndex(self, index):
        self.sidebar.setCurrentIndex(index)

    @pyqtSlot(int)
    def changeQuestion(self, index):
        self.sidebar.currentQuestionIndex = index
        self.sidebar.hintsAndHelpTab.currentQuestionIndex = index
        self.sidebar.hintsAndHelpTab.clearHints()


    """
    changes the question when previous or next button are clicked
    :param object name of signal sender
    """
    def changeQuestionIndex(self):
        sender = self.sender()
        questionListLen = len(self.questionList)

        if sender.objectName() == "previousbutton":
            if self.currentQuestionIndex == 0:
                self.currentQuestionIndex = questionListLen - 1
            else:
                self.currentQuestionIndex -= 1
        elif sender.objectName() == "nextbutton":
            self.currentQuestionIndex = (self.currentQuestionIndex + 1) % questionListLen

        self.changeQuestionSignal.emit(self.currentQuestionIndex)

        self.updateQuestionInformation()

    """
    define any signals that need to be used
    """
    def defineSignalConnections(self):
        self.changePageIndex.connect(self.changePageIndexFunction)
        self.sidebar.userCode.connect(self.sidebar.on_run_code)
        self.changeQuestionSignal.connect(self.changeQuestion)
        self.sidebarIndexSignal.connect(self.setSideBarIndex)

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

        self.questionBrowserNavAction = self.createAction("Question Browser", self.index1_emit, "Crtl+2", "Navigate to Question Browser")

        self.testPageNavAction = self.createAction("&Testing Page", self.index0_emit, "Ctrl+1", "Navigate to testing screen")

        self.menuBar.addAction(self.testPageNavAction)
        self.menuBar.addAction(self.questionBrowserNavAction)

    """
    defines the page layout
    add any layout functionality here
    """
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

    """
    defines the sidebar Widget
    the sidebar widget is a custom widget that was defined in another class, this area is responsible for instantiting it
    """
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
        self.questionInfoButton.setObjectName("questioninfobutton")
        self.questionInfoButton.clicked.connect(self.sidebar_index_emit)

        self.hintsAndHelpButton = QPushButton("Hints and Help")
        self.hintsAndHelpButton.setMinimumSize(QSize(100, 50))
        self.hintsAndHelpButton.setObjectName("hintsandhelpbutton")
        self.hintsAndHelpButton.clicked.connect(self.sidebar_index_emit)


    """
    define stylesheets
    """
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

    """
    updates text fields within the applications page
    """
    def updateQuestionInformation(self):

        self.questionTitleLabel.setText(qc.questionList[self.currentQuestionIndex].title)
        self.textEdit.setText(qc.questionList[self.currentQuestionIndex].initialFunction)
        self.sidebar.setQuestionInfo(qc.questionList[self.currentQuestionIndex].questionInformation)
        self.status.showMessage("You Switched to {}".format(qc.questionList[self.currentQuestionIndex].title), 3000)

        # initialize hints section here as well




