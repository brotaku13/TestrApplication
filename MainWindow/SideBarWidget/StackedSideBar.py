from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MainWindow.questionClassPackage import questionClass as qc

import sys
import os
import importlib



class Sidebar(QStackedWidget):


    currentQuestionIndex = 0

    userCode = pyqtSignal(str)

    save_path = "C:\\Users\\brian\\Documents\\Programming\\Python\\python projects\\TestrApplication\\MainWindow\\SideBarWidget"

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
        self.outputBox.setLineWrapMode(QTextEdit.NoWrap)

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
            self.showError(str(e))



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
            self.showError(str(e))
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

        # need to know variable number, type, if the function exists etc...
        #  inspect module

        if qc.questionList[self.currentQuestionIndex].functionName in dir(userCode):
            functionIndex = dir(userCode).index(qc.questionList[self.currentQuestionIndex].functionName)

        function = eval("userCode." + dir(userCode)[functionIndex])

        self.outputBox.setText("outputting user code...\n")
        self.outputBox.append("Input\t| \tExpected\t| \tRecieved\t| \tCorrect")
        for variables, expected in qc.questionList[self.currentQuestionIndex].testingDict.items():
            correct = False
            if len(variables) == 1:
                userResult = function(variables[0])
                if userResult == expected:
                    correct = True
                self.outputBox.append("{}\t| \t{}\t| \t{}\t| \t{}".format(str(variables[0]), str(expected), str(userResult), str(correct)))



    def showError(self, exception):
        errorMsg = QMessageBox()
        errorMsg.setIcon(QMessageBox.Warning)
        errorMsg.setWindowTitle("Exception Detected")
        errorMsg.setText(exception)
        errorMsg.exec_()













