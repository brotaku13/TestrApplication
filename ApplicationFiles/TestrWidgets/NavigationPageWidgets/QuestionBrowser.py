from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import ApplicationFiles.Resources.QuestionClass as qc
import sys

class QuestionBrowser(QWidget):

    questionSelectedSignal = pyqtSignal(int)
    changePageSignal = pyqtSignal(int)

    def __init__(self, parent=None):

        super(QuestionBrowser, self).__init__(parent)
        self.resize(900, 500)

        self.table = QTableWidget(len(qc.questionList), 2)

        self.questionTitle = QLabel("Question Title")
        font = QFont()
        font.setPointSize(16)
        self.questionTitle.setFont(font)
        self.questionInfo = QTextEdit("question information")
        self.questionInfo.setReadOnly(True)

        #  use these two to eliminate frames and borders
        #self.questionInfo.viewport().setAutoFillBackground(False)
        #self.questionInfo.setFrameStyle(QFrame.NoFrame)

        self.goToQuestionBtn = QPushButton("Go to Question")
        self.goToQuestionBtn.clicked.connect(self.emit_new_question_selected)

        self.defineLayout()


    def defineLayout(self):

        questionInfoSide = QVBoxLayout()
        questionInfoSide.addWidget(self.questionTitle)
        questionInfoSide.addWidget(self.questionInfo)

        buttonLayout = QHBoxLayout()
        buttonSpacer = QSpacerItem(20, 100, QSizePolicy.Expanding, QSizePolicy.Preferred)
        buttonLayout.addItem(buttonSpacer)
        buttonLayout.addWidget(self.goToQuestionBtn)

        questionInfoSide.addLayout(buttonLayout)
        questionListSide = QVBoxLayout()
        questionListSide.addWidget(self.table)

        totalLayout = QHBoxLayout()
        totalLayout.addLayout(questionListSide)
        totalLayout.addLayout(questionInfoSide)

        self.setLayout(totalLayout)
        self.defineTable()

    def defineTable(self):

        #define items in list
        for i in range(len(qc.questionList)):
            newTitle = QTableWidgetItem(qc.questionList[i].title)
            questionType = QTableWidgetItem(qc.questionList[i].type)
            self.table.setItem(i, 0, newTitle)
            self.table.setItem(i, 1, questionType)

        # define horizontal headers
        horHeaders = ["Question", "Type"]
        self.table.setHorizontalHeaderLabels(horHeaders)

        # hide vertical headers (no numbers)
        self.table.verticalHeader().hide()

        # resize headers
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)

        # hide grid
        self.table.setShowGrid(False)

        # select rows instead of individual cells
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.itemSelectionChanged.connect(self.questionSelected)


    def emit_new_question_selected(self):
        self.questionSelectedSignal.emit(qc.currentQuestionIndex)
        self.changePageSignal.emit(1)


    def questionSelected(self):
        row = self.table.currentRow()
        itemText = self.table.item(row, 0).text()

        index = 0
        for i in range(len(qc.questionList)):
            if qc.questionList[i].title == itemText:
                index = i
                break
        qc.currentQuestionIndex = index
        self.questionTitle.setText(qc.questionList[index].title)
        self.questionInfo.setText(qc.questionList[index].questionInformation)


"""
app = QApplication(sys.argv)
form = QuestionBrowser()
form.show()
sys.exit(app.exec_())
"""




