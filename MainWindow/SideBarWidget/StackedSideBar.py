from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MainWindow.questionClassPackage import questionClass as qc

import os
import importlib



class Sidebar(QStackedWidget):

    currentQuestionIndex = 0  #current question index initially set to zer0
                                # may need to change with time... maybe reset to question left off at
                                # changed in MainWindow when prev/next button are pressed

    userCode = pyqtSignal(str)  #  signal to collect code user writes from the coding window in the MainWindow class

    #  this will have to be changed per user machine. please open the file where this python file is stored and copy the address here
    save_path = "C:\\Users\\brian\\Documents\\Programming\\Python\\python projects\\TestrApplication\\MainWindow\\SideBarWidget"

    firstRun = True  # checks to see if userCode module needs to be reloaded

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
        self.outputBox.setReadOnly(True)

        # run code pushButton
        self.runCodeButton = QPushButton("Run Code")

        # setting up the layout
        infoLayout = QVBoxLayout()
        infoLayout.addWidget(self.questionInfoLabel)
        infoLayout.addWidget(self.questionTextBox)
        infoLayout.addWidget(self.outputTitleLabel)
        infoLayout.addWidget(self.outputBox)
        infoLayout.addWidget(self.runCodeButton)

        self.questionInfoTab.setLayout(infoLayout)

    """
    slot which collects the users code and runs the saveCode and RunCode function
    throws exception e if code does not run
    """
    @pyqtSlot(str)
    def on_run_code(self, output):
        self.saveCode(output)
        try:
            self.importAndRunCode()
            os.remove(self.filePath)
        except Exception as e:
            self.showError(str(e))

    """
    sets the question information to be displayed to the user
    :param question information text
    """
    def setQuestionInfo(self, info):
        self.questionTextBox.setText(info)


    """
    saves the code to a file called userCode.py
    throws Exception e if file cannot be saved
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

        # checks to see if the function Name is in the directory of usercode
        # basically this makes sure the user didnt rerwrite the function
        # if he changed the function statement at all then this shows an error dialog
        if qc.questionList[self.currentQuestionIndex].functionName in dir(userCode):
            functionIndex = dir(userCode).index(qc.questionList[self.currentQuestionIndex].functionName)

            # this iis where the magic happens. converting the users code into a function we can call in this widget
            function = eval("userCode." + dir(userCode)[functionIndex])

            # outputting usercode using predefined tests and recieved versus expected result
            self.outputBox.setText("outputting user code...\n")
            testsPassed = 0.0
            testNumber = 1
            for variables, expected in qc.questionList[self.currentQuestionIndex].testingDict.items():
                correct = False
                if len(variables) == 1:
                    userResult = function(variables[0])
                    if userResult == expected:
                        correct = True
                        testsPassed += 1
                    #self.outputBox.append("{}\t| \t{}\t| \t{}\t| \t{}".format(str(variables[0]), str(expected), str(userResult), str(correct)))
                    self.outputBox.append("Test {}:".format(testNumber))
                    self.outputBox.append("\tInput: {}".format(str(variables[0])))
                    self.outputBox.append("\tExpected: {}".format(str(expected)))
                    self.outputBox.append("\tRecieved: {}".format(str(userResult)))
                    self.outputBox.append("\tPassed: {}".format(str(correct)))
                    testNumber += 1

                elif len(variables) == 2:
                    userResult = function(variables[0], variables[0])
                    if userResult == expected:
                        correct = True
                    self.outputBox.append("Test {}:".format(testNumber))
                    self.outputBox.append("\tInput: {}, {}".format(str(variables[0], str(variables[1]))))
                    self.outputBox.append("\tExpected: {}".format(str(expected)))
                    self.outputBox.append("\tRecieved: {}".format(str(userResult)))
                    self.outputBox.append("\tPassed: {}".format(str(correct)))
                    testNumber += 1

            #outputs user text. this can be extended to keep track of questions correctly answered as well as percentage answered
            self.outputBox.append("\nTests passed: {:.2f}%".format((testsPassed / len(qc.questionList[self.currentQuestionIndex].testingDict))* 100))
        else:
            self.showError("Function was not found. Do not delete the function.")

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













