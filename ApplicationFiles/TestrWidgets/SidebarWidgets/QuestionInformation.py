from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import ApplicationFiles.Resources.QuestionClass as qc

class QuestionInformation(QWidget):

    def __init__(self, parent=None):
        super(QuestionInformation, self).__init__(parent)

        # setting up question information
        self.questionInfoLabel = QLabel("Question Information: ")
        labelFont = QFont()
        labelFont.setPointSize(12)
        labelFont.setFamily("Trebuchet MS")
        self.questionInfoLabel.setFont(labelFont)
        self.questionInfoLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        # Question information...
        self.questionTextBox = QTextEdit()
        self.questionTextBox.setText(qc.questionList[qc.currentQuestionIndex].questionInformation)
        self.questionTextBox.setReadOnly(True)

        # Example Label
        self.exampleLabel = QLabel("Example: ")
        self.exampleLabel.setFont(labelFont)
        self.exampleLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        # Example Information
        self.exampleTextBox = QTextEdit()
        self.exampleTextBox.setText(qc.questionList[qc.currentQuestionIndex].example)
        self.exampleTextBox.setReadOnly(True)

        # output title label
        self.outputTitleLabel = QLabel("Output Generated:")
        self.outputTitleLabel.setFont(labelFont)
        self.outputTitleLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        # output box will go here

        """
        self.outputBox = QTextEdit()
        self.outputBox.setMinimumHeight(400)
        self.outputBox.setLineWrapMode(QTextEdit.NoWrap)
        self.outputBox.setText("Output will be generated here")
        self.outputBox.setReadOnly(True)
        """


        self.report = QTableWidget()
        self.report.setMinimumHeight(400)
        self.report.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # run code pushButton


        # setting up the layout
        infoLayout = QVBoxLayout()
        infoLayout.addWidget(self.questionInfoLabel)
        infoLayout.addWidget(self.questionTextBox)
        infoLayout.addWidget(self.exampleLabel)
        infoLayout.addWidget(self.exampleTextBox)
        infoLayout.addWidget(self.outputTitleLabel)
        infoLayout.addWidget(self.report)


        self.setLayout(infoLayout)


