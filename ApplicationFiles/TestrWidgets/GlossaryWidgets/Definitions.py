from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from bs4 import BeautifulSoup
import requests
from PyQt5.QtWebEngineWidgets import *


class Definitions(QWidget):

    def __init__(self, parent=None):


        self.web = QWebEngineView()
        self.web.setMaximumWidth(450)
        self.web.setMaximumHeight(380)

        super(Definitions, self).__init__(parent)
        self.resize(1300, 900)

        self.table = QTableWidget()
        self.table.setMaximumWidth(450)

        self.definitionTitle = QLabel("Explanation")
        self.termTitle = QLabel("Concepts")

        font = QFont()
        font.setPointSize(16)
        self.definitionTitle.setFont(font)
        self.termTitle.setFont(font)

        self.definitionInfo = QTextBrowser()

        self.definitionInfo.setOpenLinks(True)
        self.definitionInfo.setOpenExternalLinks(True)
        self.definitionInfo.setReadOnly(True)

        self.URLDict = self.getURLItems()
        self.defineLayout()

    def defineLayout(self):

        questionInfoSide = QVBoxLayout()
        questionInfoSide.addWidget(self.definitionTitle)
        questionInfoSide.addWidget(self.definitionInfo)

        self.hyperlinkLabel = QLabel('<a href="http://stackoverflow.com/">Need more help?</a>')
        self.hyperlinkLabel.setOpenExternalLinks(True)
        questionInfoSide.addWidget(self.hyperlinkLabel)

        questionListSide = QVBoxLayout()
        questionListSide. addWidget(self.termTitle)
        questionListSide.addWidget(self.table)
        questionListSide.addWidget(self.web)

        #place holder for embedded hyperlink
        self.tablespacer = QSpacerItem(100, 500, QSizePolicy.Expanding, QSizePolicy.Preferred)

        totalLayout = QHBoxLayout()
        totalLayout.addLayout(questionListSide)
        totalLayout.addLayout(questionInfoSide)

        self.setLayout(totalLayout)
        self.defineTable()

    def getURLItems(self):
        url = "https://docs.python.org/3/tutorial/"
        r = requests.get(url)
        data = r.text

        soup = BeautifulSoup(data, "html.parser")

        div = soup.find('div', {'class', 'toctree-wrapper compound'})  # returns soup object meeting the certain class requirements
        links = div.find_all('a', class_='reference internal')  ## returns list of links for index


        pages = [link for link in links if link.get_text().split(' ')[0].count('.') == 1]
        linkDict = {}
        for link in pages:
            linkDict[link.get_text()] = link.get('href')

        print(linkDict)  # now have a dictionary of titles and links {link : link title}
        return linkDict

    def defineTable(self):

        termList = [title for title in self.URLDict.keys()]

        self.table.setRowCount(len(termList))
        self.table.setColumnCount(1)
        for i in range(len(termList)):
            dictItem = QTableWidgetItem(termList[i][termList[i].index(' ') + 1:])
            self.table.setItem(i, 0, dictItem)

        self.table.horizontalHeader().hide()
        # hide vertical headers (no numbers)
        self.table.verticalHeader().hide()

        # resize headers
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)

        # hide grid
        self.table.setShowGrid(False)

        # select rows instead of individual cells
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.itemSelectionChanged.connect(self.definitionSelected)

    def definitionSelected(self):
        #determining which item has been selected

        #Weblist for the video URLs
        webList = [""""""]
        ######

        currentItemIndex = self.table.currentRow()
        pageList = [page for page in self.URLDict.keys()]

        #getting soup object
        url = "https://docs.python.org/3/tutorial/" + self.URLDict[pageList[currentItemIndex]]
        print(url)
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, "html.parser")

        ##finding the text and setting it
        id = pageList[currentItemIndex].lower()
        id = id.replace(':', '') ## hacky solution to a problem...ew
        id = id.replace('?', '')
        id = id[id.index(' ') + 1:]
        id = id.replace(' ', '-')
        divs = soup.find("div", {"id" : id})

        pageText = divs.get_text().replace('Â¶', '')


        self.definitionInfo.setText(pageText)

        htmlString = """<iframe width="460" height="315" src="http://www.youtube.com/embed/ZDa-Z5JzLYM?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>"""

        self.web.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.web.page().fullScreenRequested.connect(lambda request: request.accept())
        baseUrl = "local"
        self.web.setHtml(htmlString, QUrl(baseUrl))


