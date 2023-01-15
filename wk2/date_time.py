# Date/time
from datetime import date, datetime, time

today = date.today()
print(today)

# Date object
tomorrow = date(2023, 1, 16)
print(tomorrow)

next_week = date.fromisoformat('2023-01-22')
print(next_week)

# Time stamp
    # Current
right_now = date = datetime.now()
print(right_now)
    # Number of seconds
print(right_now.timestamp())

# Convert timestamp to date objects
my_date = datetime.fromtimestamp(1500000000)
print(my_date)

afternoon = time(16, 25, 3)
print (afternoon)