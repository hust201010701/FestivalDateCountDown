# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Window.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import button_rc
from datetime import date

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        self.currentRow = 0
        self.currentColumn = -1
        self.maxColumn = 10
        self.stateList = list()
        self.buttonList = list()
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(914, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(500, 100))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 914, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        self.pushButton.clicked.connect(self.calculate)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "节日倒计时 - by orzanglei v1.0"))
        self.pushButton.setText(_translate("mainWindow", "计算倒计时"))


    def addWidgetIntoGridLayout(self,text,state):
        button = QtWidgets.QPushButton(text)

        if self.currentColumn < self.maxColumn - 1:
            self.currentColumn = self.currentColumn + 1
        else:
            self.currentRow = self.currentRow + 1
            self.currentColumn = 0
        if state:
            button.setStyleSheet("background-image:url(:checkbox/checked.png)")
        else:
            button.setStyleSheet("background-image:none")
        button.setObjectName(str(self.currentRow*self.maxColumn + self.currentColumn))
        button.clicked.connect(lambda: self.changeState(int(button.objectName())))
        self.buttonList.append(button)
        self.gridLayout.addWidget(button, self.currentRow, self.currentColumn)
        self.stateList.append(state)

    def changeState(self,pos):
        for i in range(len(self.buttonList)):
            if self.stateList[i] == True:
                self.buttonList[i].setStyleSheet("background-image:url(:checkbox/checked.png)")
            else:
                self.buttonList[i].setStyleSheet("background-image:none")

        if self.stateList[pos] == True:
            self.buttonList[pos].setStyleSheet("background-image:none")
            self.stateList[pos]= False
        else:
            self.buttonList[pos].setStyleSheet("background-image:url(:checkbox/checked.png)")
            self.stateList[pos] = True

    def setFestivalList(self,allFestival):
        self.festivalList = allFestival


    def calculate(self):
        now = date.today()
        flag = True
        resultStr = "今天是"+str(now.year)+"年"+str(now.month)+"月"+str(now.day)+"日，星期"+self.getChineseStr(now.weekday())+"。今天"
        for i in range(len(self.stateList)):
            if self.stateList[i]:
                festival = self.festivalList[i]
                resultStr += "距%s还有%d天,"%(festival.getFestival(),(festival.getDate() - now).days)
            if now == self.festivalList[i].getDate() and flag:
                resultStr = "今天是" + str(now.year) + "年" + str(now.month) + "月" + str(
                    now.day) + "日，星期" + self.getChineseStr(now.weekday()) + "。今天是"+self.festivalList[i].getFestival()+"。今天"
                flag = False
        resultStr = resultStr[:-1]+"。"
        self.textEdit.clear()
        self.textEdit.append(resultStr)
        #print(resultStr)


    def getChineseStr(self,i):
        if i == 6:
            return "日"
        elif i == 0:
            return "一"
        elif i == 1:
            return "二"
        elif i == 2:
            return "三"
        elif i == 3:
            return "四"
        elif i == 4:
            return "五"
        elif i == 5:
            return "六"