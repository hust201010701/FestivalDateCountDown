from datetime import date


class DayEntity(object):
    def __init__(self,dateStr,festival,type):
        self.dateStr = "2017/"+dateStr
        self.year = int(self.dateStr.split("/")[0])
        self.month = int(self.dateStr.split("/")[1])
        self.day = int(self.dateStr.split("/")[2])
        self.festival = festival
        self.type = type

    def getDate(self):
        d = date(self.year,self.month,self.day)
        return d

    def getDateString(self):
        return str(self.year)+"年"+str(self.month)+"月"+str(self.day)+"日"

    def getFestival(self):
        return self.festival

    def getType(self):
        return self.type

