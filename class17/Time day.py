from datetime import date,time,datetime

day = date.today()
daytoday = datetime.now()


print("the day today is",day)
print("the day now is",daytoday)

print("the date now is",daytoday.day,daytoday.month,daytoday.year)