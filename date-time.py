# Date and Time

import datetime
# from datetime import datetime
d = datetime.date(2017, 7, 24)
print(d)

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.day)
# Monday=0, Sunday=6
print(tday.weekday())
# Monday=1, Sunday=7
print(tday.isoweekday())

# Adding Time delate to know difference between two dates
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - tdelta)

# Adding a date to a date to get Time delta
bday = datetime.date(2019, 5, 27)
till_bday = bday - tday
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())

# Working with time, minutes and seconds
t = datetime.time(9, 30, 45, 1000)
print(t)
print(t.hour)

dt = datetime.datetime(2019, 5, 27, 12, 00, 00, 10000)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)

tdelta = datetime.timedelta(hours=7)
print(dt + tdelta)

# Alternative constructors
dt_today = datetime.datetime.today()
print(dt_today)
dt_now = datetime.datetime.now()
print(dt_now)
dt_utcnow = datetime.datetime.utcnow()
print(dt_utcnow)

# Difference between today() and now() is today() returns date time with timezone 0, now() give options to input timezone, nothing given, takes 0 as timezone
