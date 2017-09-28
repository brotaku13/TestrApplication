
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
        self.example = ""


questionList = []

# Brian done
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
isUnique.hint1 = "How can you iterate through a string? Keep in mind there are more ways to go through a string.\n\n"
isUnique.hint2 = "How can you tell if a string has more than one of the same character?\n\n"
isUnique.hint3 = "Try using a nested loop to iterate through the string and compare each character to all the characters before it.\n\n"
isUnique.example = "\"abc\" is a unique string while \"aaa\" is not."
questionList.append(isUnique)

# Brian done
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
URLify.hint1 = "How can you tell if a string has a space in it?\n\n"
URLify.hint2 = "How can you insert a string into another string?\n\n"
URLify.hint3 = "Try building a string and when you encounter a space add '%20' instead of the whitespace.\n\n"
questionList.append(URLify)

# Nhat done
conversion = Question()
conversion.title = "Bit Manipulation"
conversion.functionName = "bitSwapRequired"
conversion.variables = ["num1", "num2"]
conversion.initialFunction = "def {}({}, {}):".format(conversion.functionName, conversion.variables[0],
                                                      conversion.variables[1])
conversion.questionInformation = "Write a function to determine the number of bits you would need to flip to convert integer A to integer B. " \
                                 "\nEXAMPLE \nInput: 29 (or: 11101), 15 (or: 01111) \nOutput: 2"
conversion.type = conversion.questionTypeList[4]
conversion.testingDict = {("11101",): 29,
                          ("1000011",): 67,
                          ("1110010",): 114,
                          ("11111111",): 255}
conversion.hint1 = "Remember binary numbers are : 2^4 + 2^3 + 2^2 + 0 + 2^0 = 29?\n\n"
conversion.hint2 = "How can you compare if one bit is different that another one?\n\n"
conversion.hint3 = "Think about what an XOR indicates. If you do a XOR b, where does the result have 1s? Where does it have Os?\n\n"
questionList.append(conversion)

# jonathon done
tripleStep = Question()
tripleStep.title = "Triple Step"
tripleStep.functionName = "tripleStep"
tripleStep.variables = ["num"]
tripleStep.initialFunction = "def {}({}):".format(tripleStep.functionName, tripleStep.variables[0])
tripleStep.questionInformation = "A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs. Return an integer."
tripleStep.type = tripleStep.questionTypeList[0]
tripleStep.testingDict = {(19,): 66012,
                          (10,): 274,
                          (1,): 1,
                          (11,): 504,
                          (20,): 121415,
                          (0,): 1}
tripleStep.hint1 = "How can you calculate all the possibilities that can be made?\n\n"
tripleStep.hint2 = "Try using a recusive function to calculate all the possibilities and return 1 when there are no more steps to take\n\n"
tripleStep.hint3 = "Add the recursivve possibilities together and instead of multiplying them\n\n"

questionList.append(tripleStep)

# jonathon done
romanInteger = Question()
romanInteger.title = "Roman to Integer"
romanInteger.functionName = "romanInteger"
romanInteger.variables = ["numeral"]
romanInteger.initialFunction = "def {}({}):".format(romanInteger.functionName, romanInteger.variables[0])
romanInteger.questionInformation = "Given a roman numeral, convert it to an integer. Return an integer."
romanInteger.type = romanInteger.questionTypeList[0]
romanInteger.testingDict = {("IX",): 9,
                            ("XC",): 90,
                            ("XXIV ",): 24,
                            ("CXCI",): 191,
                            ("MCMXC",): 1990,
                            ("MCMLIV",): 1954}
romanInteger.hint1 = "Did you get all the possible conversions? Remember I placed before V or X indicates one less, so four is IV (one less than five) and nine is IX (one less than ten)\n\n"
romanInteger.hint2 = "X placed before L or C indicates ten less, so forty is XL (ten less than fifty) and ninety is XC (ten less than a hundred)\n\n"
romanInteger.hint3 = "C placed before D or M indicates a hundred less, so four hundred is CD (a hundred less than five hundred) and nine hundred is CM (a hundred less than a thousand)\n\n"

questionList.append(romanInteger)

# carlos
oneAway = Question()
oneAway.title = "One Away"
oneAway.functionName = "oneAway"
oneAway.variables = ["str", "str"]
oneAway.initialFunction = "def {} ({}) :".format(oneAway.functionName, oneAway.variables[0], oneAway.variables[1])
oneAway.questionInformation = "There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character." \
                              "Given two strings, write a function to check if they are one edit(or zero edits) away."
oneAway.type = oneAway.questionTypeList[0]
oneAway.testingDict = {("pale", "ple"): True,
                       ("pales", "pale"): True,
                       ("play", "tray"): False,
                       ("pale", "bake"): False,
                       ("bullet", "bulets"): False}
oneAway.hint1 = "Count the number of changes being made to the string. Only is true if there are 1 or less edits made to the string."
oneAway.hint2 = "Try using the length of the string in your algorithm to determine if there were any changes."
oneAway.hint3 = "Check to make sure that you are iterating through the string properly."
questionList.append(oneAway)

# carlos
twoSum = Question()
twoSum.title = "Two Sum"
twoSum.functionName = "twoSum"
twoSum.variables = ["intList", "int"]
twoSum.initialFunction = "def {} ({}) :".format(twoSum.functionName, twoSum.variables[0], twoSum.variables[1])
twoSum.questionInformation = "Given an array of integers, return indices of the two numbers such that they add up to a specific target." \
                             "You may assume that each input would have exactly one solution, and you may not use the same element twice."
twoSum.type = twoSum.questionTypeList[5]
twoSum.testingDict = {(1, 2, 3, 4, 5): 9,
                      (5, 17, 23, 92): 40,
                      (242, 123, 42, 578, 76): 199,
                      (2, 3, 5, 7, 9, 11, 13, 17): 8}

twoSum.hint1 = "How can you compare all the elements in an array to see if they add up to the target?"
twoSum.hint2 = "Trying using a nested for loop to iterate through the array and add all the combination of elements together."
twoSum.hint3 = "Try subtracting the elements of the array from the number to try and find it."
questionList.append(twoSum)


