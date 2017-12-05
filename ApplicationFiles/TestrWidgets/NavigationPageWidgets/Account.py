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
        self.pictureLabel.setMaximumHeight(250)
        self.pictureLabel.setMaximumWidth(250)

        userNameFont = QFont()
        userNameFont.setPointSize(30)
        userNameFont.setFamily("Helvetica")
        userNameFont.setBold(True)

        nameFont = QFont()
        nameFont.setPointSize(20)
        nameFont.setFamily("Helvetica")

        infoFont = QFont()
        infoFont.setPointSize(16)
        infoFont.setFamily("Helvetica")

        self.username = QLabel(save.getInfo("username"))
        self.username.setFont(userNameFont)

        self.firstName = QLabel(save.getInfo("firstName"))
        self.firstName.setFont(nameFont)

        self.lastName = QLabel(save.getInfo("lastName"))
        self.lastName.setFont(nameFont)

        self.email = QLabel(save.getInfo("email"))
        self.email.setFont(nameFont)

        self.questionsCompletedLabel = QLabel("Questions completed: {}".format(save.getProblemsSolved()))
        self.questionsCompletedLabel.setFont(infoFont)

        self.recentsLabel = QLabel("Recent Activity")
        self.recentsLabel.setFont(infoFont)
        self.recentsTable = QTableWidget(10, 2)
        self.recentsTable.setMaximumWidth(400)

        self.recentsTable.verticalHeader().hide()
        header = self.recentsTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)

        horHeaders = ["Question", "Date"]
        self.recentsTable.setHorizontalHeaderLabels(horHeaders)

        self.recentsTable.setShowGrid(False)
        self.recentsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.recentsTable.setSelectionBehavior(QAbstractItemView.SelectRows)


        self.defineLayout()
        self.updateTable()

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

    def updateTable(self):

        problemHistory = save.getProblemHistory()

        inProgress = QColor(247, 222, 148)
        completed = QColor(143, 224, 162)

        self.recentsTable.clearContents()
        self.recentsTable.setRowCount(len(problemHistory))

        for i in range(len(problemHistory)):
            log = problemHistory[i].split(':')
            problem = QTableWidgetItem(log[0])
            date = QTableWidgetItem(log[2])

            if log[1] ==  'True':
                problem.setBackground(completed)
                date.setBackground(completed)
            else:
                problem.setBackground(inProgress)
                date.setBackground(inProgress)

            self.recentsTable.setItem(i, 0, problem)
            self.recentsTable.setItem(i, 1, date)

    @pyqtSlot()
    def callUpdateTable(self):
        self.updateTable()

    @pyqtSlot()
    def updateQuestionsSolved(self):
        self.questionsCompletedLabel.setText("Questions completed: {}".format(save.getProblemsSolved()))





'''
app = QApplication(sys.argv)
form = Account()
form.show()
sys.exit(app.exec_())
'''



