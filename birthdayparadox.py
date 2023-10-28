import random
import datetime
birthday=[]
i=0
while(i<50):
    year=random.randint(1895,2023)
    if(year%4==0 and year%100!=0 and year%400==0):
        leap=1
    else:
        leap=0
    month=random.randint(1,12)
    if(month==2):
        if(leap==1):
            date=random.randint(1,29)
        else:
            date=random.randint(1,28)
    if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        date=random.randint(1,31)
    if(month==4 or month==6 or month==9 or month==11):
        date=random.randint(1,30)
    i=i+1
    dd=datetime.date(year,month,date)
    day_of_year=dd.timetuple().tm_yday
    birthday.append(day_of_year)
birthday.sort()
i=0
while(i<50):
    print(birthday[i])
    i=i+1
    