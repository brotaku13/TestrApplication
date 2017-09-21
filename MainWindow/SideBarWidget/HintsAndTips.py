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

        self.showHint2 = QPushButton("Show Hint 2")
        self.showHint2.setObjectName("hint2button")

        self.showHint3 = QPushButton("Show hint 3")
        self.showHint3.setObjectName("hint3button")

        self.hint1View = QTextEdit()
        self.hint1View.setReadOnly(True)

        self.hint2View = QTextEdit()
        self.hint2View.setReadOnly(True)

        self.hint3View = QTextEdit()
        self.hint3View.setReadOnly(True)

        self.defineButtonActions()
        self.defineLayout()


    def defineLayout(self):
        hint1VLayout = QVBoxLayout()
        hint1VLayout.addWidget(self.showHint1)
        hint1VLayout.addWidget(self.hint1View)
        hint1HLayout = QHBoxLayout()
        hint1HLayout.addLayout(hint1VLayout)

        hint2VLayout = QVBoxLayout()
        hint2VLayout.addWidget(self.showHint2)
        hint2VLayout.addWidget(self.hint2View)
        hint2HLayout = QHBoxLayout()
        hint2HLayout.addLayout(hint2VLayout)

        hint3VLayout = QVBoxLayout()
        hint3VLayout.addWidget(self.showHint3)
        hint3VLayout.addWidget(self.hint3View)
        hint3HLayout = QHBoxLayout()
        hint3HLayout.addLayout(hint3VLayout)

        totalLayout = QVBoxLayout()
        totalLayout.addLayout(hint1HLayout)
        vspacer1 = QSpacerItem(20, 100, QSizePolicy.Expanding, QSizePolicy.Preferred)
        totalLayout.addItem(vspacer1)

        totalLayout.addLayout(hint2HLayout)
        vspacer2 = QSpacerItem(20, 100, QSizePolicy.Expanding, QSizePolicy.Preferred)
        totalLayout.addItem(vspacer2)

        totalLayout.addLayout(hint3HLayout)


        self.setLayout(totalLayout)

    def defineButtonActions(self):
        self.showHint1.clicked.connect(self.revealHint)
        self.showHint2.clicked.connect(self.revealHint)
        self.showHint3.clicked.connect(self.revealHint)


    """
    reveals hint based upon which button was clicked
    """
    def revealHint(self):

        sender = self.sender()
        if sender.objectName() == "hint1button":
            self.hint1View.setText(qc.questionList[self.currentQuestionIndex].hint1)
        elif sender.objectName() == "hint2button":
            self.hint2View.setText(qc.questionList[self.currentQuestionIndex].hint2)
        else:
            self.hint3View.setText(qc.questionList[self.currentQuestionIndex].hint3)

    """
    clears hints when the question index is changed
    """
    def clearHints(self):

        self.hint1View.clear()
        self.hint2View.clear()
        self.hint3View.clear()

