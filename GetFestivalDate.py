import requests
from bs4 import BeautifulSoup
from DayEntity import *
from Window import *
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

result = requests.get("http://tools.2345.com/jieri.htm")
html_data = result.content.decode("gb2312")
soup = BeautifulSoup(html_data,"html5lib")
year = soup.find("div",class_ = "jieri")
clearfix = year.find_all("dl",class_="clearfix")
allFestival = list()

for month in clearfix:
    days = month.find("dd").find("ul").find_all("li")
    for day in days:
        a_tag = day.find("a")
        type = "中国传统节日"
        if "cRed" in str(a_tag["class"]):
            type = "中国传统节日"
        elif "cGreen" in str(a_tag["class"]):
            type = "公众 / 国际节日"
        elif "cBlue" in str(a_tag["class"]):
            type = "24节气"
        else:
            type = "中国传统节日"
        dayEntity = DayEntity(day.text.split("[")[1][:-1],day.text.split("[")[0],type)
        allFestival.append(dayEntity)

allFestival.append(DayEntity("6/7","2017高考","中国传统节日"))
allFestival.append(DayEntity("12/24", "2017考研", "中国传统节日"))

now = date.today()

class MainWindow(QMainWindow):
    def __init__(self,allFestival,parent = None):
        QMainWindow.__init__(self,parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.setFestivalList(allFestival)
        for festival in allFestival:
            text = festival.getFestival()+"\n"+festival.getDateString()
            left_date = festival.getDate() - now
            if left_date.days > 0  and left_date.days < 30 and festival.getType() != "公众 / 国际节日":
                self.ui.addWidgetIntoGridLayout(text,True)
            else:
                self.ui.addWidgetIntoGridLayout(text, False)

app = QApplication(sys.argv)
mainWindow = MainWindow(allFestival)
mainWindow.show()
app.exec_()