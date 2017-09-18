from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
import os
import importlib



class Sidebar(QStackedWidget):

    userCode = pyqtSignal(str)

    save_path = "C:/Users/Brian/Documents/school/PythonProjects/Testr/MainWindow/SideBarWidget"

    firstRun = True

    def __init__(self, parent=None):
        super(QStackedWidget, self).__init__(parent)
        self.questionInfoTab = QWidget()
        self.hintsAndHelpTab = QWidget()
        self.addWidget(self.questionInfoTab)
        self.addWidget(self.hintsAndHelpTab)

        # setting up question information
        self.questionInfoLabel = QLabel("Question Information: ")
        labelFont = QFont()
        labelFont.setPointSize(20)
        labelFont.setFamily("Trebuchet MS")
        self.questionInfoLabel.setFont(labelFont)
        self.questionInfoLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        #Question information...
        self.questionTextBox = QTextEdit(self.questionInfoTab)
        self.questionTextBox.setText("put question information here....")
        self.questionTextBox.setReadOnly(True)

        #output title label
        self.outputTitleLabel = QLabel("Output Generated:")
        self.outputTitleLabel.setFont(labelFont)
        self.outputTitleLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        #output box will go here
        self.outputBox = QTextEdit(self.questionInfoTab)
        self.outputBox.setText("output will be generated here")

        # run code pushButton
        self.runCodeButton = QPushButton("Run Code")


        infoLayout = QVBoxLayout()
        infoLayout.addWidget(self.questionInfoLabel)
        infoLayout.addWidget(self.questionTextBox)
        infoLayout.addWidget(self.outputTitleLabel)
        infoLayout.addWidget(self.outputBox)
        infoLayout.addWidget(self.runCodeButton)

        self.questionInfoTab.setLayout(infoLayout)

    @pyqtSlot(str)
    def on_run_code(self, output):
        self.saveCode(output)
        try:
            self.importAndRunCode()
            os.remove(self.filePath)
        except Exception as e:
            print(e)

    def setQuestionInfo(self, info):
        self.questionTextBox.setText(info)


    """
    saves the code
    """
    def saveCode(self, userCode):
        self.filePath = os.path.join(self.save_path, "userCode.py")
        try:
            userFile = open(self.filePath, "w")
            userFile.write(userCode)
            userFile.close()

        except Exception as e:
            print(e)

    """
    import the code into the current system
    reloads the module after any editing takes place
    sets the output text
    """
    def importAndRunCode(self):
        from MainWindow.SideBarWidget import userCode
        if self.firstRun:
            self.firstRun = False
        else:
            importlib.reload(userCode)


        result = userCode.isUnique()

        if result is str:
            self.outputBox.setText(result)
        else:
            self.outputBox.setText(str(result))











