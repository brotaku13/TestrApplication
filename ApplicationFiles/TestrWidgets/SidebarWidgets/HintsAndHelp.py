from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import ApplicationFiles.Resources.QuestionClass as qc

class HintsAndHelp(QWidget):

    def __init__(self, parent=None):
        super(HintsAndHelp, self).__init__(parent)

        self.showHint = QPushButton("Show Hint 1")
        self.showHint.setObjectName("hint1button")

        self.example = QPushButton("Show Example")
        self.example.setObjectName("exampleButton")

        self.showAnswer = QPushButton("Show Answer")
        self.showAnswer.setObjectName("answerButton")

        self.hintView = QTextEdit()
        self.hintView.setReadOnly(True)

        self.exampleView = QTextEdit()
        self.exampleView.setReadOnly(True)

        self.answerView = QTextEdit()
        self.answerView.setReadOnly(True)

        self.defineButtonActions()
        self.defineLayout()

    def defineLayout(self):
        hint1VLayout = QVBoxLayout()
        hint1VLayout.addWidget(self.showHint)
        hint1VLayout.addWidget(self.hintView)
        hint1HLayout = QHBoxLayout()
        hint1HLayout.addLayout(hint1VLayout)

        exampleLayout = QVBoxLayout()
        exampleLayout.addWidget(self.example)
        exampleLayout.addWidget(self.exampleView)
        exampleLayout1 = QHBoxLayout()
        exampleLayout1.addLayout(exampleLayout)

        answerLayout = QVBoxLayout()
        answerLayout.addWidget(self.showAnswer)
        answerLayout.addWidget(self.answerView)
        answerLayout1 = QHBoxLayout()
        answerLayout1.addLayout(answerLayout)

        totalLayout = QVBoxLayout()
        totalLayout.addLayout(hint1HLayout)
        vspacer1 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Preferred)  # second number is space between all text boxes and such?
        totalLayout.addItem(vspacer1)

        totalLayout.addLayout(exampleLayout1)
        vspacer2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Preferred)
        totalLayout.addItem(vspacer2)

        totalLayout.addLayout(answerLayout1)

        self.setLayout(totalLayout)

    def defineButtonActions(self):
        self.showHint.clicked.connect(self.revealHint)
        self.example.clicked.connect(self.revealHint)
        self.showAnswer.clicked.connect(self.revealHint)

    """
    reveals hint based upon which button was clicked
    """

    def revealHint(self):

        sender = self.sender()
        if sender.objectName() == "hint1button" and qc.questionList[qc.currentQuestionIndex].hintNumber < 3:
            self.hintView.append("***Hint {}***\n".format(qc.questionList[qc.currentQuestionIndex].hintNumber + 1))
            self.hintView.append(qc.questionList[qc.currentQuestionIndex].hintList[qc.questionList[qc.currentQuestionIndex].hintNumber])
            qc.questionList[qc.currentQuestionIndex].hintShown[qc.questionList[qc.currentQuestionIndex].hintNumber] = True
            qc.questionList[qc.currentQuestionIndex].hintNumber += 1


        elif sender.objectName() == "exampleButton":
            self.exampleView.setText(qc.questionList[qc.currentQuestionIndex].example)

        elif sender.objectName() == "answerButton":
            self.answerView.setText(qc.questionList[qc.currentQuestionIndex].answer)

    def resetHints(self):
        self.hintView.clear()
        hintIndex = 0
        for hintRevealed in qc.questionList[qc.currentQuestionIndex].hintShown:
            if hintRevealed:
                self.hintView.append("***Hint {}***\n".format(qc.questionList[qc.currentQuestionIndex].hintList[hintIndex]))
                hintIndex += 1

        self.exampleView.clear()



