import ApplicationFiles.Resources.filepaths as path
import os
import ApplicationFiles.Resources.QuestionClass as qc

accountPath = ""

def saveAccount(userName):
    global accountPath
    userDirectory = os.path.join(path.UsersDirectory, userName)

    if os.path.isdir(userDirectory):
        accountPath = userDirectory

    else:
        os.makedirs(userDirectory)

def saveCode(code):

    #get name of file
    filename = qc.questionList[qc.currentQuestionIndex].title + ".txt"
    filename = filename.replace(" ", "")

    #completeName
    codeFilePath = os.path.join(accountPath, filename)

    try:
        saveText = open(codeFilePath, "w")
        saveText.write(code)
        saveText.close()
    except Exception as e:
        print(e)

def openCode():
    filename = qc.questionList[qc.currentQuestionIndex].title + ".txt"
    filename = filename.replace(" ", "")

    # completeName
    codeFilePath = os.path.join(accountPath, filename)

    file = open(codeFilePath, "r")
    code = ""
    for line in file:
        code += line

    return code

def checkExists(questionTitle):
    filename = qc.questionList[qc.currentQuestionIndex].title + ".txt"
    filename = filename.replace(" ", "")
    
    # completeName
    codeFilePath = os.path.join(accountPath, filename)

    return os.path.isfile(codeFilePath)