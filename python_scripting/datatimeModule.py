import datetime as dt

# print(dt.date.today())

now = dt.datetime.today()

other = dt.datetime(1994,10, 10,17,59)
print(now-other)