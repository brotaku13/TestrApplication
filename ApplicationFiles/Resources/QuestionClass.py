class Question():

    def __init__(self):
        self.questionTypeList = ["Arrays and Strings", "Linked Lists", "Stacks and Queues", "Trees and Graphs",
                                 "Bit Manipulation", "Math and Logic Puzzles", "Object oriented Design",
                                 "Recursion", "Sorting and Searching"]

        self.questionInformation = "Information goes here"
        self.functionName = ""
        self.variables = []
        self.initialFunction = ""
        self.title = "Question Title"
        self.type = ""
        self.testingDict = {}
        self.hint1 = ""
        self.hint2 = ""
        self.hint3 = ""
        self.hintList = []
        self.example = ""
        self.hintNumber = 0
        self.hintShown = [False, False, False]
        self.answerShown = False
        self.answer = ""
        self.hyperlink = ""


questionList = []
currentQuestionIndex = 0

# Brian done
isUnique = Question()
isUnique.title = "Is Unique"
isUnique.functionName = "isUnique"
isUnique.variables = ["str"]
isUnique.initialFunction = "def {}({}):".format(isUnique.functionName, isUnique.variables[0])
isUnique.questionInformation = "Implement an algorithm to determine if a string has all unique characters. Return a boolean value."
isUnique.type = isUnique.questionTypeList[0]
isUnique.testingDict = {("abcd",): True,
                        ("2nf Frt",): True,
                        ("aaaa78c ",): False,
                        ("12345as",): True,
                        ("AsdF 658",): True,
                        ("test",): False}
isUnique.hintList.append("How can you iterate through a string? Keep in mind there are more ways to go through a string.\n")
isUnique.hintList.append("How can you tell if a string has more than one of the same character?\n")
isUnique.hintList.append("Try using a nested loop to iterate through the string and compare each character to all the characters before it.\n")
isUnique.example = "\"abc\" is a unique string while \"aaa\" is not."
isUnique.answer = "# Assuming character set is ASCII (128 characters)\n    i" \
"f len(str) > 128:\n        return False\n\n    char_set = [False for _ in range" \
"(128)]\n    for char in str:\n        val = ord(char)\n        if char_set[val]" \
":\n            # Char already found in string\n            return False\n        c" \
"har_set[val] = True\n\n    return True"
isUnique.hyperlink = '<a href="https://www.youtube.com/watch?v=UqEU-obRUnI">Need more help?</a>'
questionList.append(isUnique)


# Brian done
URLify = Question()
URLify.title = "URLify"
URLify.functionName = "URLify"
URLify.variables = ["string"]
URLify.initialFunction = "def {}({}):".format(URLify.functionName, URLify.variables[0])
URLify.type = isUnique.questionTypeList[0]
URLify.questionInformation = "Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold all" \
                             "additional characters, and that you are given the 'True' length of the string. return a string"
URLify.type = URLify.questionTypeList[0]
URLify.testingDict = {("Coding is Fun",): "Coding%20is%20Fun",
                      ("Here is another test",): "Here%20is%20another%20test",
                      ("much ado about nothing      ",): "much%20ado%20about%20nothing",
                      ("Mr John Smith    ",): "Mr%20John%20Smith"}
URLify.hintList.append("How can you tell if a string has a space in it?\n")
URLify.hintList.append("How can you insert a string into another string?\n")
URLify.hintList.append("Try building a string and when you encounter a space add '%20' instead of the whitespace.\n")
URLify.example = "For instance, \"Interviews are important!\" will become \"Interviews%20are%20important!\""
URLify.answer = URLify.answer = "import string\nimport re\n\ndef URLify(string):\n\tstring = string.strip()\n\tstring = re.sub(r\"[\s+]\", '%20', string)\n\n\treturn string"
URLify.hyperlink = '<a href="https://www.youtube.com/watch?v=IlsikVwUffI">Need more help?</a>'
questionList.append(URLify)



#Nhat done
conversion = Question()
conversion.title = "Bit Manipulation"
conversion.functionName = "bitSwapRequired"
conversion.variables = ["num1", "num2"]
conversion.initialFunction = "def {}({}, {}):".format(conversion.functionName, conversion.variables[0], conversion.variables[1])
conversion.questionInformation = "Write a function to determine the number of bits you would need to flip to convert integer A to integer B. "
conversion.type = conversion.questionTypeList[4]
conversion.testingDict = {("11101", "10011"): 3,
                          ("1000011", "1111111"): 4,
                          ("1110010", "1010101"): 4,
                          ("11111111", "00000000"): 8}
conversion.hintList.append("Remember binary numbers are : 2^4 + 2^3 + 2^2 + 0 + 2^0 = 29?\n")
conversion.hintList.append("How can you compare if one bit is different that another one?\n")
conversion.hintList.append("Think about what an XOR indicates. If you do a XOR b, where does the result have 1s? Where does it have Os?\n")
conversion.example = "Input: 29 (or: 11101), 15 (or: 01111) \nOutput: 2"
conversion.answer = "Answer goes here"
conversion.hyperlink = '<a href="https://www.youtube.com/watch?v=frwqnS9ICxw">Need more help?</a>'
questionList.append(conversion)


#jonathon done
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
tripleStep.hintList.append("How can you calculate all the possibilities that can be made?\n")
tripleStep.hintList.append("Try using a recusive function to calculate all the possibilities and return 1 when there are no more steps to take\n")
tripleStep.hintList.append("Add the recursivve possibilities together and instead of multiplying them\n")
tripleStep.example = "Example Goes here"
tripleStep.answer = "def tripleStep(num):\n\tif num < 0:\n\t\treturn 0\n\tif num == 0:\n\t\treturn 1\n\tif num == 1" \
":\n\t\treturn 1\n\treturn tripleStep(num - 1) + tripleStep(num - 2) + rripleStep(num -" \
" 3)\n\n\ndef Method2(num):\n\tmemo = [-1] * (num + 1)\n\treturn TripleHopRecursive(num, memo" \
")\n\n\ndef TripleHopRecursive(num, memo):\n\tif num < 0:\n\t return 0\n\tmemo[0] = 1\n" \
"\tif x >= 1:\n\t memo[1] = 1\n\tif num >= 2:\n\t memo[2] = memo[1] + memo[" \
"0]\n\tif num > 2:\n\t\tfor i in range(3, num + 1):\n\t\t\tmemo[i] = memo[i - 1] + memo[i - 2" \
"] + memo[i - 3]\n\treturn memo[num]"
tripleStep.hyperlink = '<a href="https://www.youtube.com/watch?v=urF1XreNtXI">Need more help?</a>'
questionList.append(tripleStep)

#jonathon done
romanInteger = Question()
romanInteger.title = "Roman to Integer"
romanInteger.functionName = "romanInteger"
romanInteger.variables = ["num"]
romanInteger.initialFunction = "def {}({}):".format(romanInteger.functionName, romanInteger.variables[0])
romanInteger.questionInformation = "Given a roman numeral, convert it to an integer. Return an integer."
romanInteger.type = romanInteger.questionTypeList[0]
romanInteger.testingDict = {("IX",): 9,
                            ("XC",): 90,
                            ("XXIV ",): 24,
                            ("CXCI",): 191,
                            ("MCMXC",): 1990,
                            ("MCMLIV",): 1954}
romanInteger.hintList.append("Did you get all the possible conversions? Remember I placed before V or X indicates one less, so four is IV (one less than five) and nine is IX (one less than ten)\n")
romanInteger.hintList.append("X placed before L or C indicates ten less, so forty is XL (ten less than fifty) and ninety is XC (ten less than a hundred)\n")
romanInteger.hintList.append("C placed before D or M indicates a hundred less, so four hundred is CD (a hundred less than five hundred) and nine hundred is CM (a hundred less than a thousand)\n")
romanInteger.example = "The roman numeral 14 is expressed as XIV, so given this numeral, the function would return 14."
romanInteger.answer = "Answer goes here."
romanInteger.hyperlink = '<a href="https://www.youtube.com/watch?v=os4x1oFB9iY">Need more help?</a>'
questionList.append(romanInteger)


# carlos
oneAway = Question()
oneAway.title = "One Away"
oneAway.functionName = "oneAway"
oneAway.variables = ["str1", "str2"]
oneAway.initialFunction = "def {} ({}, {}) :".format(oneAway.functionName, oneAway.variables[0], oneAway.variables[1])
oneAway.questionInformation = "There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character." \
                               "Given two strings, write a function to check if they are one edit(or zero edits) away. Return True if str1 is either 0 or 1 edit away from str2, or False if it is greator than 1 edit away. "
oneAway.type = oneAway.questionTypeList[0]
oneAway.testingDict = {("pale", "ple"): True,
                       ("pales", "pale"): True,
                       ("play", "tray"): False,
                       ("pale", "bake"): False,
                       ("bullet", "bulets"): False}
oneAway.hintList.append("Count the number of changes being made to the string. Only is true if there are 1 or less edits made to the string.")
oneAway.hintList.append("Try using the length of the string in your algorithm to determine if there were any changes.")
oneAway.hintList.append("Check to make sure that you are iterating through the string properly.")
oneAway.example = "if str1 = 'Coding' and str2 = 'Coing, then you would return True, as the two strings are only 1 edit away (inserting d). Also, if str1 = 'Tester' and str2 = 'tastr' then you would return false, as there are two edits that would need to be performed."
oneAway.answer = ""
oneAway.hyperlink = '<a href="https://www.youtube.com/watch?v=nYFd7VHKyWQ">Need more help?</a>'
questionList.append(oneAway)



charCounter = Question()
charCounter.title = "charCut"
charCounter.functionName = "charCut"
charCounter.variables = ["str1"]
charCounter.initialFunction = "def {}({}):".format(charCounter.functionName, charCounter.variables[0])
charCounter.questionInformation = "given the string, return the string without the first letter"
charCounter.type = charCounter.questionTypeList[0]
charCounter.testingDict = {("heye", ): "eye",
                           ("hellol", ): "ellol",
                           ("abc", ): "bc",
                           ("jello",): "ello",
                           ("haha", ): "aha"}
charCounter.hintList.append("Try doing it one statement")
charCounter.hintList.append("Use a return")
charCounter.hintList.append("Slice the string!")
charCounter.example = "For instance, if you have the word 'Coding', it would return 'oding'"
charCounter.answer = "return str1[1:]"
charCounter.hyperlink = '<a href="https://www.youtube.com/watch?v=k9TUPpGqYTo">Need more help?</a>'
questionList.append(charCounter)
