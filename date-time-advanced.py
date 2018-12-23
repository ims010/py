import datetime

d = datetime.date(2018, 12, 5)  # No leading zeros
print(d)

tdy = datetime.date.today()
print(tdy)
print(tdy.year)
print(tdy.day)

# Day of the week
print(tdy.weekday()) # Weekday, Monday is 0, Sunday is 6
print(tdy.isoweekday()) # ISOWeekday, Monday is 1, Sunday is 7


