import ApplicationFiles.Resources.filepaths as path
import os
import ApplicationFiles.Resources.QuestionClass as qc
from shutil import copy2
import datetime

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


def createnewAccountInfo(firstName, lastName, email, username, picturePath=''):
    global accountPath

    if picturePath != '':
        copy2(picturePath, accountPath)

        file = picturePath.split('/')
        pictureFileName = os.path.join(accountPath, file[-1])
    else:
        pictureFileName = ""


    infoList = [firstName, lastName, email, username]
    with open(accountPath + "\\AccountInfo.txt", 'w') as file:
        infoLine = ';'.join(infoList)

        file.write("info: " + infoLine + '\n')
        file.write("PicturePath: " + pictureFileName + '\n')
        file.write("ProblemsSolved: 0" + '\n')
        file.write("RecentProblems")


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

def getProblemsSolved():
    global accountPath
    accountInfoPath = os.path.join(accountPath, "AccountInfo.txt")

    with open(accountInfoPath, 'r') as file:
        lines = file.readlines()
        info = lines[2].split(' ')

        return info[1]

def incrementProblemsSolved():
    global accountPath
    accountInfoPath = os.path.join(accountPath, "AccountInfo.txt")

    lines = open(accountInfoPath, 'r').readlines()
    info = lines[2].split(' ')
    numProblems = int(info[1].strip())
    numProblems += 1
    lines[2] = "{} {}\n".format(info[0], numProblems)
    out = open(accountInfoPath, 'w')
    out.writelines(lines)
    out.close()

def writeProblemsSolved(problemTitle, correct):
    global accountPath
    now = datetime.datetime.now()
    accountInfoPath = os.path.join(accountPath, "AccountInfo.txt")
    lines = open(accountInfoPath, 'r').readlines()
    recentProblems = lines[3].split(';')

    date = '{}/{}/{}'.format(now.month, now.day, now.year)
    problemLog = '{}:{}:{}'.format(problemTitle, correct, date)
    # 'title:True/False:11/26/2017'

    doesNotexist = True

    if len(recentProblems) > 1:
        for i in range(1, len(recentProblems)):
            log = recentProblems[i].split(':')
            if log[0] == problemTitle:
                doesNotexist = False
                if len(recentProblems) < 12:
                    recentProblems.pop(i)
                    recentProblems.insert(1, problemLog)

                else:
                    recentProblems.insert(1, problemLog)
                    recentProblems.pop(-1)
                break

    if doesNotexist:
        if len(recentProblems) < 12:
            recentProblems.insert(1, problemLog)
        else:
            recentProblems.insert(1, problemLog)
            recentProblems.pop(-1)

    logString = ';'.join(recentProblems)

    out = open(accountInfoPath, 'w')
    lines[3] = logString
    out.writelines(lines)
    out.close()

def getProblemHistory():
    global accountPath
    accountInfoPath = os.path.join(accountPath, "AccountInfo.txt")
    file = open(accountInfoPath, 'r')
    lines = file.readlines()
    file.close()
    recentProblems = lines[3].split(';')
    if len(recentProblems) > 1:
        return recentProblems[1:]
    else:
        return []














