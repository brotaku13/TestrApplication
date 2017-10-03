from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Testr.ApplicationFiles.TestrWidgets.SidebarWidgets.HintsAndHelp import HintsAndHelp
from Testr.ApplicationFiles.TestrWidgets.SidebarWidgets.QuestionInformation import QuestionInformation
import Testr.ApplicationFiles.Resources.QuestionClass as qc
import Testr.ApplicationFiles.Resources.filepaths as path
import os
import importlib


class Sidebar(QWidget):

    firstRun = True

    def __init__(self, parent=None):
        super(Sidebar, self).__init__(parent)
        self.sidebarPages = QStackedWidget()

        self.hintsAndHelpTab = HintsAndHelp()
        self.questionInformationTab = QuestionInformation()
        self.sidebarPages.addWidget(self.questionInformationTab)
        self.sidebarPages.addWidget(self.hintsAndHelpTab)

        self.runCodeButton = QPushButton("Run Code")


        self.defineLayout()

    def defineLayout(self):
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.sidebarPages)
        vlayout.addWidget(self.runCodeButton)
        self.setLayout(vlayout)

    def updateQuestionInformation(self):
        self.questionInformationTab.questionTextBox.setText(qc.questionList[qc.currentQuestionIndex].questionInformation)
        self.questionInformationTab.exampleTextBox.setText(qc.questionList[qc.currentQuestionIndex].example)
        self.hintsAndHelpTab.resetHints()

    @pyqtSlot(str)
    def runUserCode(self, code):
        self.saveCode(code)
        try:
            self.importAndRunCode()
            os.remove(self.filePath)
        except Exception as e:
            self.showError(str(e))


    def saveCode(self, userCode):
        self.filePath = os.path.join(path.userCodeSavePath, "userCode.py")
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
        from Testr.ApplicationFiles.Resources import userCode

        if self.firstRun:
            self.firstRun = False
        else:
            importlib.reload(userCode)

        # checks to see if the function Name is in the directory of usercode
        # basically this makes sure the user didnt rerwrite the function
        # if he changed the function statement at all then this shows an error dialog
        if qc.questionList[qc.currentQuestionIndex].functionName in dir(userCode):
            functionIndex = dir(userCode).index(qc.questionList[qc.currentQuestionIndex].functionName)

            # this iis where the magic happens. converting the users code into a function we can call in this widget
            function = eval("userCode." + dir(userCode)[functionIndex])

            # outputting usercode using predefined tests and recieved versus expected result
            self.questionInformationTab.outputBox.setText("outputting user code...\n")
            testsPassed = 0.0
            testNumber = 1
            for variables, expected in qc.questionList[qc.currentQuestionIndex].testingDict.items():
                correct = False
                if len(variables) == 1:
                    userResult = function(variables[0])
                    if userResult == expected:
                        correct = True
                        testsPassed += 1

                    # self.outputBox.append("{}\t| \t{}\t| \t{}\t| \t{}".format(str(variables[0]), str(expected), str(userResult), str(correct)))
                    self.questionInformationTab.outputBox.append("Test {}:".format(testNumber))
                    self.questionInformationTab.outputBox.append("\tInput: {}".format(str(variables[0])))
                    self.questionInformationTab.outputBox.append("\tExpected: {}".format(str(expected)))
                    self.questionInformationTab.outputBox.append("\tRecieved: {}".format(str(userResult)))
                    self.questionInformationTab.outputBox.append("\tPassed: {}".format(str(correct)))
                    testNumber += 1

                elif len(variables) == 2:
                    userResult = function(variables[0], variables[1])
                    if userResult == expected:
                        correct = True
                    self.questionInformationTab.outputBox.append("Test {}:".format(testNumber))
                    self.questionInformationTab.outputBox.append("\tInput: {}, {}".format(str(variables[0], str(variables[1]))))
                    self.questionInformationTab.outputBox.append("\tExpected: {}".format(str(expected)))
                    self.questionInformationTab.outputBox.append("\tRecieved: {}".format(str(userResult)))
                    self.questionInformationTab.outputBox.append("\tPassed: {}".format(str(correct)))
                    testNumber += 1

            # outputs user text. this can be extended to keep track of questions correctly answered as well as percentage answered
            self.questionInformationTab.outputBox.append("\nTests passed: {:.2f}%".format((testsPassed / len(qc.questionList[qc.currentQuestionIndex].testingDict)) * 100))
        else:
            self.showError("Function was not found. Do not delete the original function name.")

    """
    executes an error dialog box...effectively acts as a debugger of sorts for the user.... albeit not a very good one
    :param the exception which will be displayed..
    """

    def showError(self, exception):
        errorMsg = QMessageBox()
        errorMsg.setIcon(QMessageBox.Warning)
        errorMsg.setWindowTitle("Exception Detected")
        errorMsg.setText(exception)
        errorMsg.exec_()







