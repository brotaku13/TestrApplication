from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import ApplicationFiles.Resources.QuestionClass as qc



class Definitions(QWidget):

#not sure if these are needed
    questionSelectedSignal = pyqtSignal(int)
    changePageSignal = pyqtSignal(int)

    definitionTermList = ["Lists", "Loops", "Functions", "Classes"]
                #LISTS
    definitionInfoList = ["The most basic data structure in Python is the sequence. Each element of a sequence is assigned a number - its position or index. "
                          "The first index is zero, the second index is one, and so forth.\n\nPython has six built-in types of sequences, "
                          "but the most common ones are lists and tuples, which we would see in this tutorial.\nThere are certain things you can do with all sequence types. "
                          "These operations include indexing, slicing, adding, multiplying, and checking for membership. In addition, "
                          "Python has built-in functions for finding the length of a sequence and for finding its largest and smallest elements."
                          "\n\nThe list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. "
                          "Important thing about a list is that items in a list need not be of the same type.\n\nCreating a list is as simple as putting different comma-separated values between square brackets. "
                          "\n\nFor example −\n\n"
                          "list1 = [ \'physics\' ,  \'chemistry\' , 1997 , 2000];\nlist2 = [ 1 , 2 , 3 , 4 , 5 ];\nlist3 = "
                          "[ \"a\" , \"b\" , \"c\" , \"d\"]",
               #LOOPS
                          "In general, statements are executed sequentially: The first statement in a funct"
                          "ion is executed first, followed by the second, and so on. There may be a situat"
                          "ion when you need to execute a block of code several number of times.\n\nProgrammi"
                          "ng languages provide various control structures that allow for more complicated"
                          " execution paths.\n\nA loop statement allows us to execute a statement or group of"
                          " statements multiple times.\n"
                          "\nWhile loops - "
                          "Repeats a statement or group of statements while a given condition is TRUE. It t"
                          "ests the condition before executing the loop body.\n"
                          "\nFor loops - "
                          "Executes a sequence of statements multiple times and abbreviates the code that m"
                          "anages the loop variable\n"
                          "\nNested loops - "
                          "You can use one or more loop inside any another while, for or do..while loop",
                #FUNCTION
                          "A function is a block of organized, reusable code that is used to perform a sing"
                          "le, related action. Functions provide better modularity for your application an"
                          "d a high degree of code reusing.\n\nAs you already know, Python gives you many bui"
                          "lt-in functions like print(), etc. but you can also create your own functions. "
                          "These functions are called user-defined functions."
                          "You can define functions to provide the required functionality. Here are simple "
                          "rules to define a function in Python.\n\nFunction blocks begin with the keyword de"
                          "f followed by the function name and parentheses (  ).\n\nAny input parameters o"
                          "r arguments should be placed within these parentheses. You can also define para"
                          "meters inside these parentheses.\n\nThe first statement of a function can be an op"
                          "tional statement - the documentation string of the function or docstring.\n\nThe c"
                          "ode block within every function starts with a colon : and is indented.\n\nThe st"
                          "atement return [expression] exits a function, optionally passing back an expres"
                          "sion to the caller. A return statement with no arguments is the same as return "
                          "None.\n\n"
                          "def functionname( parameters ):\n   function_suite\n   return [expression]"
                          "\n\nThe following function takes a string as input parameter and prints it on standa"
                          "rd screen.\n\n"
                          "def printme( str ):\n   #This prints a passed string into this function\n   print(str)\n   return",
                 #CLASSES
                          "Python has been an object-oriented language since it existed. Because of this, c"
                          "reating and using classes and objects are downright easy. This chapter helps yo"
                          "u become an expert in using Python's object-oriented programming support.\n\nIf yo"
                          "u do not have any previous experience with object-oriented (OO) programming, yo"
                          "u may want to consult an introductory course on it or at least a tutorial of so"
                          "me sort so that you have a grasp of the basic concepts.\n\nHowever, here is small "
                          "introduction of Object-Oriented Programming (OOP) to bring you at speed.\n\n"
                          "Class − A user-defined prototype for an object that defines a set of attributes "
                          "that characterize any object of the class. The attributes are data members (cla"
                          "ss variables and instance variables) and methods, accessed via dot notation.\n\n"
                          "Class variable − A variable that is shared by all instances of a class. Class va"
                          "riables are defined within a class but outside any of the class's methods. Clas"
                          "s variables are not used as frequently as instance variables are.\n\n"
                          "Data member − A class variable or instance variable that holds data associated w"
                          "ith a class and its objects.\n\n"
                          "Instance variable − A variable that is defined inside a method and belongs only "
                          "to the current instance of a class.\n\n"
                          "Instance − An individual object of a certain class. An object obj that belongs t"
                          "o a class Circle, for example, is an instance of the class Circle.\n\n"
                          "Object − A unique instance of a data structure that's defined by its class. An o"
                          "bject comprises both data members (class variables and instance variables) and "
                          "methods.\n\nAn example of a python class below.\n\n"
                          "class Employee:\n   #Common base class for all employees\n   empCount = 0\n\n   def"
                          " __init__(self, name, salary):\n      self.name = name\n      self.salary = salar"
                          "y\n      Employee.empCount += 1\n   \n   def displayCount(self):\n     print(\"Total"
                          " Employee %d\") % Employee.empCount\n\ndef displayEmployee(self): \n    print(\"Name : \", self.name, \", Salary: \", self.salary)"
                          ]

    def __init__(self, parent=None):

        super(Definitions, self).__init__(parent)
        self.resize(1000, 700)

        self.table = QTableWidget(len(self.definitionTermList), 1)

        self.definitionTitle = QLabel("Definitions")
        self.termTitle = QLabel("Terms")
        font = QFont()
        font.setPointSize(16)
        self.definitionTitle.setFont(font)
        self.termTitle.setFont(font)
        self.definitionInfo = QTextEdit("definition information")
        self.definitionInfo.setReadOnly(True)

        self.defineLayout()

    def defineLayout(self):

        questionInfoSide = QVBoxLayout()
        questionInfoSide.addWidget(self.definitionTitle)
        questionInfoSide.addWidget(self.definitionInfo)

        self.hyperlinkLabel = QLabel('<a href="http://stackoverflow.com/">Need more help?</a>')
        self.hyperlinkLabel.setOpenExternalLinks(True)
        questionInfoSide.addWidget(self.hyperlinkLabel)

        questionListSide = QVBoxLayout()
        questionListSide. addWidget(self.termTitle)
        questionListSide.addWidget(self.table)

        totalLayout = QHBoxLayout()
        totalLayout.addLayout(questionListSide)
        totalLayout.addLayout(questionInfoSide)

        self.setLayout(totalLayout)
        self.defineTable()

    def defineTable(self):

        #define items in list
        for i in range(len(self.definitionTermList)):
            newTitle = QTableWidgetItem(self.definitionTermList[i])
            self.table.setItem(i, 0, newTitle)

        self.table.horizontalHeader().hide()
        # hide vertical headers (no numbers)
        self.table.verticalHeader().hide()

        # resize headers
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)

        # hide grid
        self.table.setShowGrid(False)

        # select rows instead of individual cells
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.itemSelectionChanged.connect(self.definitionSelected)

#don't think this is needed?
    def emit_new_question_selected(self):
        self.questionSelectedSignal.emit(qc.currentQuestionIndex)
        self.changePageSignal.emit(1)


    def definitionSelected(self):
        row = self.table.currentRow()
        self.definitionInfo.setText(self.definitionInfoList[row])





