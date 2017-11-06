from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import ApplicationFiles.Resources.QuestionClass as qc

class HintsAndHelp(QWidget):

    changeToGlossary = pyqtSignal(int)


    def __init__(self, parent=None):
        super(HintsAndHelp, self).__init__(parent)

        self.showHint = QPushButton("Show Hint")
        self.showHint.setObjectName("hint1button")


        self.showAnswer = QCheckBox("Show Answer")
        self.showAnswer.setObjectName("answerButton")

        self.hintView = QTextEdit()
        self.hintView.setReadOnly(True)

        self.glossary = QPushButton("Glossary")

        self.hyperLinkLabel = QLabel("Hyperlink Here")
        self.hyperLinkLabel.setOpenExternalLinks(True)
        self.hyperLinkLabel.setAlignment(Qt.AlignRight | Qt.AlignBottom)


        self.answerView = QTextEdit()
        self.answerView.setMinimumHeight(400)
        textEditFont = QFont()
        textEditFont.setFamily("Consolas")
        textEditFont.setStyleHint(QFont.Monospace)
        tabMetric = QFontMetrics(textEditFont)
        tabSpace = tabMetric.width("M" * 5)
        self.answerView.setTabStopWidth(tabSpace)
        self.answerView.setLineWrapMode(QTextEdit.NoWrap)
        self.answerView.setReadOnly(True)

        self.defineButtonActions()
        self.defineLayout()

    def defineLayout(self):
        hint1VLayout = QVBoxLayout()
        hint1VLayout.addWidget(self.hintView)

        glossaryHelp = QHBoxLayout()
        glossaryHelp.addWidget(self.showHint)
        glossaryHelp.addWidget(self.glossary)
        glossaryHelp.addWidget(self.hyperLinkLabel)

        hint1VLayout.addLayout(glossaryHelp)

        hint1HLayout = QHBoxLayout()
        hint1HLayout.addLayout(hint1VLayout)

        answerLayout = QVBoxLayout()
        answerLayout.addWidget(self.showAnswer)
        answerLayout.addWidget(self.answerView)
        answerLayout1 = QHBoxLayout()
        answerLayout1.addLayout(answerLayout)

        totalLayout = QVBoxLayout()
        totalLayout.addLayout(hint1HLayout)
        vspacer1 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Preferred)  # second number is space between all text boxes and such?
        totalLayout.addItem(vspacer1)

        vspacer2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Preferred)
        totalLayout.addItem(vspacer2)

        totalLayout.addLayout(answerLayout1)

        self.setLayout(totalLayout)

    def defineButtonActions(self):
        self.showHint.clicked.connect(self.revealHint)
        self.showAnswer.stateChanged.connect(self.stateCheck)
        self.glossary.clicked.connect(self.change_to_glossary_emit)

    def change_to_glossary_emit(self):
        self.changeToGlossary.emit(2)

    """
    reveals hint based upon which button was clicked
    """

    def stateCheck(self):
        if self.showAnswer.isChecked():
            self.answerView.setText(qc.questionList[qc.currentQuestionIndex].answer)
        else:
            self.answerView.setText('')

    def revealHint(self):

        sender = self.sender()
        if sender.objectName() == "hint1button" and qc.questionList[qc.currentQuestionIndex].hintNumber < 3:
            self.hintView.append("***Hint {}***\n".format(qc.questionList[qc.currentQuestionIndex].hintNumber + 1))
            self.hintView.append(qc.questionList[qc.currentQuestionIndex].hintList[qc.questionList[qc.currentQuestionIndex].hintNumber])
            qc.questionList[qc.currentQuestionIndex].hintShown[qc.questionList[qc.currentQuestionIndex].hintNumber] = True
            qc.questionList[qc.currentQuestionIndex].hintNumber += 1

        elif sender.objectName() == "answerButton":
            self.answerView.setText(qc.questionList[qc.currentQuestionIndex].answer)

    def resetHints(self):
        self.hintView.clear()
        hintIndex = 0
        for hintRevealed in qc.questionList[qc.currentQuestionIndex].hintShown:
            if hintRevealed:
                self.hintView.append("***Hint {}***\n".format(qc.questionList[qc.currentQuestionIndex].hintList[hintIndex]))
                hintIndex += 1




