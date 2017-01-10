from datetime import date
now = date.today()
chunjie = date(2017,1,28)  #春节的日期
chazhi = chunjie - now     #相差时间
print(chazhi.days)         #只需要知道相差时间的天数