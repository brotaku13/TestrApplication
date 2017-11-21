from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import ApplicationFiles.Resources.SaveInfo as save
import sys

class Account(QWidget):

    def __init__(self, parent=None):
        super(Account, self).__init__(parent)
        self.setMinimumHeight(450)

        self.pictureLabel = QLabel()
        self.picture = QPixmap()

        self.picture.load(save.getInfo("picturePath"))
        self.pictureLabel.setPixmap(self.picture)

        userNameFont = QFont()
        userNameFont.setPointSize(30)
        userNameFont.setFamily("Helvetica")
        userNameFont.setBold(True)

        nameFont = QFont()
        nameFont.setPointSize(20)
        nameFont.setFamily("Helvetica")



        self.username = QLabel(save.getInfo("username"))
        self.username.setFont(userNameFont)

        self.firstName = QLabel(save.getInfo("firstName"))
        self.firstName.setFont(nameFont)

        self.lastName = QLabel(save.getInfo("lastName"))
        self.lastName.setFont(nameFont)

        self.email = QLabel(save.getInfo("email"))
        self.email.setFont(nameFont)

        self.questionsCompletedLabel = QLabel("Questions completed: ")
        self.averageTimePerQuestion = QLabel("Average time per question: ")
        self.totalTime = QLabel("Total Time spent in Program: ")

        self.recentsLabel = QLabel("Recent Activity")
        self.recentsTable = QTableWidget()
        self.recentsTable.setMaximumWidth(400)

        self.defineLayout()

    def defineLayout(self):

        nameLayout = QHBoxLayout()
        nameLayout.addWidget(self.firstName)
        nameLayout.addWidget(self.lastName)
        hspacer3 = QSpacerItem(20, 50, QSizePolicy.Expanding, QSizePolicy.Preferred)
        nameLayout.addItem(hspacer3)

        userNameLayout = QVBoxLayout()
        userNameLayout.addWidget(self.username)
        userNameLayout.addLayout(nameLayout)
        userNameLayout.addWidget(self.email)

        pictureLayout = QHBoxLayout()
        pictureLayout.setSizeConstraint(QLayout.SetMinimumSize)
        pictureLayout.addWidget(self.pictureLabel)
        hspacer1 = QSpacerItem(20, 50, QSizePolicy.Expanding, QSizePolicy.Preferred)
        hspacer2 = QSpacerItem(40, 50, QSizePolicy.Minimum, QSizePolicy.Preferred)

        pictureLayout.addItem(hspacer2)
        pictureLayout.addLayout(userNameLayout)
        pictureLayout.addItem(hspacer1)

        statsLayout = QVBoxLayout()
        statsLayout.addWidget(self.questionsCompletedLabel)
        statsLayout.addWidget(self.averageTimePerQuestion)
        statsLayout.addWidget(self.totalTime)

        leftSide = QVBoxLayout()
        leftSide.addLayout(pictureLayout)
        leftSide.addLayout(statsLayout)

        rightSide = QVBoxLayout()
        rightSide.addWidget(self.recentsLabel)
        rightSide.addWidget(self.recentsTable)

        totalLayout = QHBoxLayout()
        totalLayout.addLayout(leftSide)
        totalLayout.addLayout(rightSide)

        self.setLayout(totalLayout)




'''
app = QApplication(sys.argv)
form = Account()
form.show()
sys.exit(app.exec_())
'''



