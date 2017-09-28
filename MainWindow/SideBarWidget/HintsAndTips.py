from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MainWindow.questionClassPackage import questionClass as qc


import os
import sys

class HintsAndTipsClass(QWidget):

    currentQuestionIndex = 0

    def __init__(self, parent = None):
        super(HintsAndTipsClass, self).__init__(parent)

        self.showHint1 = QPushButton("Show Hint 1")
        self.showHint1.setObjectName("hint1button")

        self.example = QPushButton("Show Example")
        self.example.setObjectName("exampleButton")

        self.showAnswer = QPushButton("Show Answer")
        self.showAnswer.setObjectName("answerButton")

        self.hint1View = QTextEdit()
        self.hint1View.setReadOnly(True)

        self.exampleView = QTextEdit()
        self.exampleView.setReadOnly(True)

        self.answerView = QTextEdit()
        self.answerView.setReadOnly(True)

        self.defineButtonActions()
        self.defineLayout()


    def defineLayout(self):
        hint1VLayout = QVBoxLayout()
        hint1VLayout.addWidget(self.showHint1)
        hint1VLayout.addWidget(self.hint1View)
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
        vspacer1 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Preferred) # second number is space between all text boxes and such?
        totalLayout.addItem(vspacer1)

        totalLayout.addLayout(exampleLayout1)
        vspacer2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Preferred)
        totalLayout.addItem(vspacer2)

        totalLayout.addLayout(answerLayout1)


        self.setLayout(totalLayout)

    def defineButtonActions(self):
        self.showHint1.clicked.connect(self.revealHint)
        self.example.clicked.connect(self.revealHint)
        self.showAnswer.clicked.connect(self.revealHint)


    """
    reveals hint based upon which button was clicked
    """
    def revealHint(self):

        sender = self.sender()
        if sender.objectName() == "hint1button":
            if qc.questionList[self.currentQuestionIndex].count == 0 :
                self.hint1View.setText(qc.questionList[self.currentQuestionIndex].hint1)
                qc.questionList[self.currentQuestionIndex].count += 1
            elif qc.questionList[self.currentQuestionIndex].count == 1 :
                self.hint1View.append(qc.questionList[self.currentQuestionIndex].hint2)
                qc.questionList[self.currentQuestionIndex].count += 1
            else:
                self.hint1View.append(qc.questionList[self.currentQuestionIndex].hint3)
                qc.questionList[self.currentQuestionIndex].count += 1
        elif sender.objectName() == "exampleButton":
            self.exampleView.setText(qc.questionList[self.currentQuestionIndex].example)
        else:
            self.answerView.setText(qc.questionList[self.currentQuestionIndex].answer)

    """
    clears hints when the question index is changed
    """
    def clearHints(self):

        self.hint1View.clear()
        self.exampleView.clear()
        self.answerView.clear()
