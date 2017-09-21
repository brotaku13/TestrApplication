
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

# Brian
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


# Brian
URLify = Question()
URLify.title = "URLify"
URLify.functionName = "URLify"
URLify.variables = ["var1"]
URLify.initialFunction = "def {}({}):".format(URLify.functionName, URLify.variables[0])
URLify.type = isUnique.questionTypeList[0]
URLify.questionInformation = "Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold all" \
                             "additional characters, and that you are given the 'True' length of the string. return a string"
URLify.type = URLify.questionTypeList[0]
URLify.testingDict = {("Coding is Fun",): "Coding%20is%20Fun",
                      ("Here is another test",): "Here%20is%20another%20test",
                      ("much ado about nothing      ",): "much%20ado%20about%20nothing",
                      ("Mr John Smith    ",): "Mr%20John%20Smith"}
URLify.hint1 = "hint1"
URLify.hint2 = "hint2"
URLify.hint3 = "hint3"
questionList.append(URLify)


#Nhat
conversion = Question()
conversion.title = "Bit Manipulation"
conversion.functionName = "bitSwapRequired"
conversion.variables = ["num1", "num2"]
conversion.initialFunction = "def {}({}, {}):".format(conversion.functionName, conversion.variables[0], conversion.variables[1])
conversion.questionInformation = "Write a function to determine the number of bits you would need to flip to convert integer A to integer B. " \
                                 "\nEXAMPLE \nInput: 29 (or: 11101), 15 (or: 01111) \nOutput: 2"
conversion.type = conversion.questionTypeList[4]
conversion.testingDict = {"something needed here"}
conversion.hint1 = "How would you figure out how many bits are different between two numbers?"
conversion.hint2 = "Think about what an XOR indicates. If you do a XOR b, where does the result have 1s? Where does it have Os?"
questionList.append(conversion)

# Nhat
deleteMiddleNode = Question()
deleteMiddleNode.title = "Delete Node"
deleteMiddleNode.functionName = "deleteMiddleNode"
deleteMiddleNode.variables = ["Node"]
deleteMiddleNode.initialFunction = "def {}({}):".format(deleteMiddleNode.functionName, deleteMiddleNode.variables[0])
deleteMiddleNode.questionInformation = "Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node. " \
                                       "\nEXAMPLE \nlnput: The node c from the linked list a->b->c->d->e->f \nResult: nothing is returned, but the new linked list looks like a->b->d->e- >f."

deleteMiddleNode.type = deleteMiddleNode.questionTypeList[1]
deleteMiddleNode.testingDict = {"something needed here"}
deleteMiddleNode.hint1 = "Picture the list 1->5->9->12. Removing 9 would make it look like 1->5->12. You only have access to the 9 node. Can you make it look like the correct answer?"

questionList.append(deleteMiddleNode)

#phil wtf
Sort_List = Question()
Sort_List.title = "Sort_list"
Sort_List.functionName = "Sort_List"
Sort_List.variables = ["str"]
Sort_List.initialFunction = "def {}({}):".format(Sort_List.functionName, Sort_List.variables[0])
Sort_List.questionInformation = "Implement an algorithm to determine if a string has all unique characters. Return a boolean value."
Sort_List.type = Sort_List.questionTypeList[0]
Sort_List.testingDict = {

(4,3,5,1,6,2): [1,2,3,4,5,6],
(5,4,3,2,1): [1,2,3,4,5],
(1,2,4,3): [1,2,3,4]
}

questionList.append(Sort_List)

#jonathon
tripleStep = Question()
tripleStep.title = "Triple Step"
tripleStep.functionName = "tripleStep"
tripleStep.variables = ["int"]
tripleStep.initialFunction = "def {}({}):".format(tripleStep.functionName, tripleStep.variables[0])
tripleStep.questionInformation = "A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs. Return an integer."
tripleStep.type = tripleStep.questionTypeList[0]
tripleStep.testingDict = {(19,): 66012,
                        (10,): 274,
                        (1,): 1,
                        (11,): 504,
                        (20,): 121415,
						(0,): 1}
tripleStep.hint1 = "Use a recursive function"
tripleStep.hint2 = "Add the recursivve possibilities together and instead of multiplying them"
tripleStep.hint3 = "hint3"

questionList.append(tripleStep)

#jonathon
romanInteger = Question()
romanInteger.title = "Roman to Integer"
romanInteger.functionName = "romanInteger"
romanInteger.variables = ["str"]
romanInteger.initialFunction = "def {}({}):".format(romanInteger.functionName, romanInteger.variables[0])
romanInteger.questionInformation = "Given a roman numeral, convert it to an integer. Return an integer."
romanInteger.type = romanInteger.questionTypeList[0]
romanInteger.testingDict = {("IX",): 9,
                        ("XC",): 90,
                        ("XXIV ",): 24,
                        ("CXCI",): 191,
                        ("MCMXC",): 1990,
                        ("MCMLIV",): 1954}
romanInteger.hint1 = "Did you get all possible conversions?"
romanInteger.hint2 = "Don't forget to return an integer!"
romanInteger.hint3 = "hint3"

questionList.append(romanInteger)


# carlos
oneAway = Question()
oneAway.title = "One Away"
oneAway.functionName = "oneAway"
oneAway.variables = ["str1" , "str2"]
oneAway.initialFunction = "def {} ({}) :".format(oneAway.functionName, oneAway.variables[0], oneAway.variables[1])
oneAway.questionInformation  = "There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character." \
                               "Given two strings, write a function to check if they are one edit(or zero edits) away."
oneAway.type = oneAway.questionTypeList[0]
oneAway.testingDict = {("pale", "ple") : True,
                    ("pales", "pale") : True,
                    ("play", "tray") : False,
                    ("pale", "bake") : False}
oneAway.hint1 = ""
oneAway.hint2 = ""
oneAway.hint3 = ""
questionList.append(oneAway)



# carlos
twoSum = Question()
twoSum.title = "Two Sum"
twoSum.functionName = "twoSum"
twoSum.variables = ["int[]", "int"]
twoSum.initialFunction = "def {} ({}) :".format(twoSum.functionName, twoSum.variables[0], twoSum.variables[1])
twoSum.questionInformation = "Given an array of integers, return indices of the two numbers such that they add up to a specific target." \
                             "You may assume that each input would have exactly one solution, and you may not use the same element twice."
twoSum.type = twoSum.questionTypeList[5]
twoSum.testingDict = {

    }

twoSum.hint1 = ""
twoSum.hint2 = ""
twoSum.hint3 = ""
questionList.append(twoSum)
