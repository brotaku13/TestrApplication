from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import ApplicationFiles.Resources.QuestionClass as qc
from .SiderbarWidget import Sidebar
import ApplicationFiles.Resources.SaveInfo as save


class CodingWindow(QWidget):
    """Coding window. Allows the user to enter their code into a text box and then sends the code over to the testing module to display the results. 
    """
    #changeQuestionSignal = pyqtSignal(int)  # signal which emits which button was pressed "previous/next"
    sidebarIndexSignal = pyqtSignal(int)
    userCodeSignal = pyqtSignal(str)
    updateReportRows = pyqtSignal()
    updateShowAnswer = pyqtSignal()

    def __init__(self, parent=None):
        super(CodingWindow, self).__init__(parent)

        self.questionTitleLabel = QLabel("Problem Title Here")
        self.questionTitleLabel.setText("Problem Title Goes Here")
        titleFont = QFont()
        titleFont.setPointSize(40)
        titleFont.setFamily("Trebuchet MS")
        self.questionTitleLabel.setFont(titleFont)
        self.questionTitleLabel.setAlignment(Qt.AlignBottom | Qt.AlignCenter)

        self.defineButtons()
        self.defineTextEdit()
        self.defineSidebar()
        self.updateQuestionInformation()
        self.defineLayout()

        #self.changeQuestionSignal.connect(self.changeQuestion)
        self.sidebarIndexSignal.connect(self.changeSideBarIndex)
        self.userCodeSignal.connect(self.sidebar.runUserCode)
        self.sidebar.runCodeButton.clicked.connect(self.emitUserCode)

    def emitUserCode(self):
        """Sends the user code over to the sidebar. 
        """
        self.userCodeSignal.emit(self.textEdit.toPlainText())

    def changeQuestionIndex(self):
        """Changes the current question when either the prev or next button are clicked on. 
        """

        sender = self.sender()
        questionListLen = len(qc.questionList)

        if sender.objectName() == "previousbutton":
            if qc.currentQuestionIndex == 0:
                qc.currentQuestionIndex = questionListLen - 1
            else:
                qc.currentQuestionIndex -= 1
        elif sender.objectName() == "nextbutton":
            qc.currentQuestionIndex = (qc.currentQuestionIndex + 1) % questionListLen

        #self.changeQuestionSignal.emit(qc.currentQuestionIndex)
        self.updateQuestionInformation()

    def sidebar_index_emit(self):
        """Changes the sidebar widgets index. 
        """

        sender = self.sender()
        if sender.objectName() == "hintsandhelpbutton":
            self.sidebarIndexSignal.emit(1)
        else:
            self.sidebarIndexSignal.emit(0)

    @pyqtSlot(int)
    def changeSideBarIndex(self, index):
        self.sidebar.sidebarPages.setCurrentIndex(index)


    def defineButtons(self):
        """Defines the button's look, feel, and actions
        """
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

    def defineTextEdit(self):
        """Defines the coding boxes look, feel, and actions. 
        """
        # setting up textEdit
        self.textEdit = QTextEdit()
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

    def defineLayout(self):
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

        self.setLayout(self.totalLayout)

    def defineSidebar(self):
        """Defines the sidebar widget as well as instantiates it. 
        """

        self.sidebar = Sidebar()
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMaximumSize(QSize(450, 16777215))

        self.questionInfoButton = QPushButton("Question Information")
        self.questionInfoButton.setMinimumSize(QSize(100, 50))
        self.questionInfoButton.setObjectName("questioninfobutton")
        self.questionInfoButton.clicked.connect(self.sidebar_index_emit)

        self.hintsAndHelpButton = QPushButton("Hints and Help")
        self.hintsAndHelpButton.setMinimumSize(QSize(100, 50))
        self.hintsAndHelpButton.setObjectName("hintsandhelpbutton")
        self.hintsAndHelpButton.clicked.connect(self.sidebar_index_emit)

    def updateQuestionInformation(self):
        """Primary update_ui feature. changes everythign when the current question's index is changed. 
        """

        self.questionTitleLabel.setText(qc.questionList[qc.currentQuestionIndex].title)

        self.sidebar.updateQuestionInformation()
        self.sidebar.hintsAndHelpTab.hyperLinkLabel.setText(qc.questionList[qc.currentQuestionIndex].hyperlink)

        if save.checkExists():
            self.textEdit.setText(save.openCode())
        else:
            self.textEdit.setText(qc.questionList[qc.currentQuestionIndex].initialFunction)

        self.updateReportRows.emit()
        self.updateShowAnswer.emit()
