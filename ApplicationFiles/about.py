import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ApplicationFiles.Resources.SaveInfo as save
from random import shuffle


class About(QWidget):
    def __init__(self):
        self.phil = "Phillip Nguyen: Born and raised in " \
                    "Southern California, he helped by keeping morale high and provided comedic relief. " \
                    "Phillip helped with the overall quirks of the project, including this 'about' operation of Testr. "

        self.brian = "Brian Caulfield: Brian is the most eager member of Testr. Hailing from Boston, Massachusetts," \
                     " Brian sure loves to work hard and program, this entire software would not be possible without him."

        self.nhat = "Nhat Le: Born in Vietnam, Nhat knows how to work hard... or rather work smart, Nhat is clever" \
                    " and is always trying to shorten code or write less or write code that is more efficient."

        self.carlos = "Carlos Jimenez: Born and raised in Santa Ana, Carlos Jimenez is very innovative." \
                      " Some of the very most vital functions of Testr were implemented by Carlos, not only that, he may be " \
                      "your boss someday."
        self.jon = "Jonathan Ishii: Jonathan was a great member of Testr, he often helped manage and clean up code" \
                   " for Testr, he also has a dog and a great smile. "

        self.five_hot_guys = [self.phil, self.brian, self.nhat, self.carlos, self.jon]
        shuffle(self.five_hot_guys)

        super().__init__()
        self.initUI()

    def initUI(self):
        QMessageBox.information(self, "About The Programmers",
                                "\tA Little About The Programmers"

                                "\n\n{}"

                                "\n\n{}"

                                "\n\n{}"

                                "\n\n{}"

                                "\n\n{}\n\n\t"
                                "© Copyright Testr 2017\n"
                                "\tAll Rights Reserved.".format(*self.five_hot_guys))


'''
App = QApplication(sys.argv)
about = About()
about.show()
sys.exit(App.exec_())
'''