import ApplicationFiles.Resources.filepaths as path
import os
import ApplicationFiles.Resources.QuestionClass as qc

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

accountPath = ""
loggedIn = False


def saveAccount(userName):
    global accountPath
    global loggedIn
    global user
    userDirectory = os.path.join(path.UsersDirectory, userName)

    if os.path.isdir(userDirectory):
        accountPath = userDirectory

    else:
        os.makedirs(userDirectory)
        accountPath = userDirectory


    loggedIn = True

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

def checkExists():

    filename = qc.questionList[qc.currentQuestionIndex].title + ".txt"
    filename = filename.replace(" ", "")

    # completeName
    codeFilePath = os.path.join(accountPath, filename)

    if not loggedIn:
        return False
    else:
        return os.path.isfile(codeFilePath)


def createnewAccountInfo(firstName, lastName, email, username, picturePath):
    global accountPath

    infoList = [firstName, lastName, email, username]
    with open(accountPath + "\\AccountInfo.txt", 'w') as file:
        infoLine = ';'.join(infoList)


        file.write("info: " + infoLine + '\n')

        file.write("PicturePath: " + picturePath + '\n')

        file.write("ProblemsSolved: 0" + '\n')
        file.write("AverageTimePerProblem: 0.00" + '\n')
        file.write("TotalTimeSpent: 0.00" + '\n')
        file.write("RecentProblems: " + '\n')


def getInfo(type):
    global accountPath
    accountInfoPath = os.path.join(accountPath, "AccountInfo.txt")

    with open(accountInfoPath, 'r') as file:
        lines = file.readlines()

        info = lines[0].split(' ')

        if type == "firstName":
            infoList = info[1].split(';')
            return infoList[0].strip()

        elif type == "lastName":
            infoList = info[1].split(';')
            return infoList[1].strip()

        elif type == "email":
            infoList = info[1].split(';')
            return infoList[2].strip()

        elif type == "username":
            infoList = info[1].split(';')
            return infoList[3].strip()

        elif type == "picturePath":
            pictureInfo = lines[1].split(' ')
            return pictureInfo[1].strip()


