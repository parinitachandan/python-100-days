import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
print(f"Year:{year}")

month = now.month
print(f"Month:{month}")

date = now.date()
print(f"Date:{date}")

time = now.ctime()
print(time)

day = now.weekday()
print(day)  # 0 - monday, 1- tuesday and so on

print(type(time))

dob = dt.datetime(year=2006, month=5, day=8, hour=5, minute=25)
print(dob)


