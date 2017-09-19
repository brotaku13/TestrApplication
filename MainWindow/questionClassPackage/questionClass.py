
class Question():

    def __init__(self):
        self.questionTypeList = ["Arrays and Strings", "Linked Lists", "Stacks and Queues", "Trees and Graphs",
                                 "Bit Manipulation", "Math and Logic Puzzles", "Object oriented Design",
                                 "Recursion", "Sorting and Searching"]

        self.questionInformation = "Information goes here"
        self.functionName = ""
        self.functionName = ""
        self.variables = []
        self.initialFunction = ""
        self.title = "Question Title"
        self.type = ""
        self.testingDict = {}
        self.hint1 = ""
        self.hint2 = ""
        self.hint3 = ""


questionList = []


isUnique = Question()
isUnique.title = "Is Unique"
isUnique.functionName = "isUnique"
isUnique.variables = ["str"]
isUnique.initialFunction = "def {}({}):".format(isUnique.functionName, isUnique.variables[0])
isUnique.questionInformation = "Implement an algorithm to determine if a string has all unique characters. Return a boolean value."
isUnique.type = isUnique.questionTypeList[0]
isUnique.testingDict = {("abcd",): True,
                        ("2nf Frt",): False,
                        ("aaaa78c ",): False,
                        ("12345as",): True,
                        ("AsdF 658",): True,
                        ("test",): False}
isUnique.hint1 = "Try a Hash Table"
isUnique.hint2 = "Could a bit vector be useful?"
isUnique.hint3 = "don't forget about the set function in python!"

questionList.append(isUnique)



URLify = Question()
URLify.title = "URLify"
URLify.functionName = "URLify"
URLify.variables = ["var1"]
URLify.initialFunction = "def {}({}):".format(URLify.functionName, URLify.variables[0])
URLify.questionInformation = "Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold all" \
                             "additional characters, and that you are given the 'True' length of the string. return a string"
URLify.type = URLify.questionTypeList[0]
URLify.testingDict = {("Coding is Fun",): "Coding%20is%20Fun",
                      ("Here is another test",): "Here%20is%20another%20test",
                      ("much ado about nothing      ",): "much%20ado%20about%20nothing",
                      ("Mr John Smith    ",): "Mr%20John%20Smith"}
URLify.hint1 = ""
URLify.hint2 = ""
URLify.hint3 = ""
questionList.append(URLify)