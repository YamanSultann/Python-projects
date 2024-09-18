from datetime import date, time, datetime

today = date.today()
now = datetime.now()
print("Today is",today)
print("It is",now,"right now")

print("\nDate components",today.year,today.month,today.day)