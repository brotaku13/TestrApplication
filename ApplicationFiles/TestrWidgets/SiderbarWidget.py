from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ApplicationFiles.TestrWidgets.SidebarWidgets.HintsAndHelp import HintsAndHelp
from ApplicationFiles.TestrWidgets.SidebarWidgets.QuestionInformation import QuestionInformation
import ApplicationFiles.Resources.QuestionClass as qc
import ApplicationFiles.Resources.filepaths as path
import ApplicationFiles.Resources.SaveInfo as save

import os
import importlib

import ApplicationFiles.Resources.filepaths as imagePath

class Sidebar(QWidget):
    """Sidebar widget. a container for the results of the question as well as hints and tips. 
    """
    firstRun = True
    updateAccountInformation = pyqtSignal()
    updateProblemsSolved = pyqtSignal()

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
        """Updates the question information based on the current question index. 
        """
        self.questionInformationTab.questionTextBox.setText(qc.questionList[qc.currentQuestionIndex].questionInformation)
        self.questionInformationTab.exampleTextBox.setText(qc.questionList[qc.currentQuestionIndex].example)
        self.hintsAndHelpTab.resetHints()

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
        self.questionInformationTab.questionDiff1.setPixmap(starPix)
        self.questionInformationTab.questionDiff1.setAlignment(Qt.AlignBottom | Qt.AlignRight)

    @pyqtSlot(str)
    def runUserCode(self, code):
        """Runs the code the user has entered into the coding window. 
        
        Arguments:
            code {str} -- the code the user has entered into the coding window. 
        """
        self.saveCode(code)
        save.saveCode(code)
        try:
            self.importAndRunCode()
            os.remove(self.filePath)
        except Exception as e:
            self.showError(str(e))


    def saveCode(self, userCode):
        """Saves the users last run code so that it reloads if the user wants to revisit the problem
        """
        self.filePath = os.path.join(path.userCodeSavePath, "userCode.py")

        try:
            userFile = open(self.filePath, "w")
            userFile.write(userCode)
            userFile.close()

        except Exception as e:
            self.showError(str(e))
            print(e)

    def importAndRunCode(self):
        """imports the code into the folder and runs it using eval
        NOTE: This code was written without knowledge of the subprocess library. If I were to redo this, I would save the users code as it's own 
        .py file and run the .py file as a subprocess with the arguments given, and then pipe the output and use diff to check it based on the 
        answer section.
        """
        from ApplicationFiles.Resources import userCode

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

            testsPassed = 0.0
            testNumber = 0

            incorrectColor = QColor(255, 178, 178)
            correctColor = QColor(143, 224, 162)

            for variables, expected in qc.questionList[qc.currentQuestionIndex].testingDict.items():
                correct = False
                if len(variables) == 1:
                    userResult = function(variables[0])
                    if userResult == expected:
                        correct = True
                        testsPassed += 1

                    expectedText = str(expected)
                    userResultText = str(userResult)
                    expectedResultItem = QTableWidgetItem(expectedText)
                    userResultItem = QTableWidgetItem(userResultText)

                    if correct:
                        expectedResultItem.setBackground(correctColor)
                        userResultItem.setBackground(correctColor)
                    else:
                        expectedResultItem.setBackground(incorrectColor)
                        userResultItem.setBackground(incorrectColor)

                    self.questionInformationTab.report.setItem(testNumber, 0, expectedResultItem)
                    self.questionInformationTab.report.setItem(testNumber, 1, userResultItem)

                elif len(variables) == 2:
                    userResult = function(variables[0], variables[1])
                    if userResult == expected:
                        correct = True

                    expectedText = str(expected)
                    userResultText = str(userResult)
                    expectedResultItem = QTableWidgetItem(expectedText)
                    userResultItem = QTableWidgetItem(userResultText)

                    if correct:
                        expectedResultItem.setBackground(correctColor)
                        userResultItem.setBackground(correctColor)
                    else:
                        expectedResultItem.setBackground(incorrectColor)
                        userResultItem.setBackground(incorrectColor)

                    self.questionInformationTab.report.setItem(testNumber, 0, expectedResultItem)
                    self.questionInformationTab.report.setItem(testNumber, 1, userResultItem)

                testNumber += 1

            self.questionInformationTab.grade.setText("{:d}%".format(int((testsPassed / testNumber) * 100)))
            correct = False
            if int((testsPassed / testNumber) * 100) == 100:
                correct = True

            save.writeProblemsSolved(qc.questionList[qc.currentQuestionIndex].title, correct)
            self.emitUpdateAccount()
            if correct:
                self.emitProblemsSolvedUpdate()
        else:
            self.showError("Function was not found. Do not delete the original function name.")

    def emitUpdateAccount(self):
        self.updateAccountInformation.emit()

    def emitProblemsSolvedUpdate(self):
        save.incrementProblemsSolved()
        self.updateProblemsSolved.emit()

    def showError(self, exception):
        """Simple dialog popup debugger. Dispays very basic debugging informaion which is parsed form the Exception that is raised when the code is run. 
        
        Arguments:
            exception {Exception} -- Exception raised when the code is run. 
        """
        errorMsg = QMessageBox()
        errorMsg.setIcon(QMessageBox.Warning)
        errorMsg.setWindowTitle("Exception Detected")
        errorMsg.setText(exception)
        errorMsg.exec_()







