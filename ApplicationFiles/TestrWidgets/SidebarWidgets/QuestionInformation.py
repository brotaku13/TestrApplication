from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import ApplicationFiles.Resources.QuestionClass as qc

#added
import ApplicationFiles.Resources.filepaths as imagePath

class QuestionInformation(QWidget):
    """shows the data related to the current question. Information such as the actual questions, examples, and the results of the user's code. 
    """
    def __init__(self, parent=None):
        super(QuestionInformation, self).__init__(parent)

        # setting up question information
        self.questionInfoLabel = QLabel("Question Information: ")
        labelFont = QFont()
        labelFont.setPointSize(12)
        labelFont.setFamily("Trebuchet MS")
        self.questionInfoLabel.setFont(labelFont)
        self.questionInfoLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        self.questionDiff1 = QLabel()
        self.diffHBox = QHBoxLayout()
        self.diffHBox.addWidget(self.questionInfoLabel)

        if(qc.questionList[qc.currentQuestionIndex].questionDifficulty == 1) :
            starPix = QPixmap(imagePath.star1)
        elif(qc.questionList[qc.currentQuestionIndex].questionDifficulty == 2) :
            starPix = QPixmap(imagePath.star2)
        elif(qc.questionList[qc.currentQuestionIndex].questionDifficulty == 3):
            starPix = QPixmap(imagePath.star3)
        elif(qc.questionList[qc.currentQuestionIndex].questionDifficulty == 4):
            starPix = QPixmap(imagePath.star4)
        elif(qc.questionList[qc.currentQuestionIndex].questionDifficulty == 5):
            starPix = QPixmap(imagePath.star5)

        starPix = starPix.scaled(150, 2000, Qt.KeepAspectRatio)
        self.questionDiff1.setPixmap(starPix)
        self.questionDiff1.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        self.diffHBox.addWidget(self.questionDiff1)

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
        self.outputTitleLabel = QLabel("Output Report:")
        self.outputTitleLabel.setFont(labelFont)
        self.outputTitleLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        #grade Label
        self.grade = QLabel("")
        self.grade.setFont(labelFont)
        self.grade.setAlignment(Qt.AlignBottom | Qt.AlignRight)


        self.report = QTableWidget(len(qc.questionList[qc.currentQuestionIndex].testingDict), 2)
        self.report.setMinimumHeight(400)
        self.report.verticalHeader().hide()
        header = self.report.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        horHeaders = ["Expected Output", "User Output"]
        self.report.setHorizontalHeaderLabels(horHeaders)

        self.report.setShowGrid(False)
        self.report.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.report.setSelectionBehavior(QAbstractItemView.SelectRows)
        # run code pushButton


        # setting up the layout
        infoLayout = QVBoxLayout()

        infoLayout.addLayout(self.diffHBox)

        infoLayout.addWidget(self.questionTextBox)
        infoLayout.addWidget(self.exampleLabel)
        infoLayout.addWidget(self.exampleTextBox)

        gradeLayout = QHBoxLayout()
        gradeLayout.addWidget(self.outputTitleLabel)
        gradeLayout.addWidget(self.grade)

        infoLayout.addLayout(gradeLayout)
        infoLayout.addWidget(self.report)

        self.setLayout(infoLayout)

    @pyqtSlot()
    def updateReportRows(self):
        """Updates the results of the user's code. 
        """

        currentRows = self.report.rowCount()
        neededRows = len(qc.questionList[qc.currentQuestionIndex].testingDict)
        self.grade.clear()

        for i in range(currentRows):
            self.report.removeRow(0)

        for i in range(neededRows):
            self.report.insertRow(self.report.rowCount())
