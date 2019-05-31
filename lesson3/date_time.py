from datetime import datetime, timedelta

day = timedelta(days=1)

today = datetime.now()

month = timedelta(days=31)

yesterday = datetime.strftime(today-day, '%Y/%m/%d')

month_ago = datetime.strftime(today-month, '%Y/%m/%d')

today_string = datetime.strftime(today, '%Y/%m/%d')

print(yesterday)
print(month_ago)
print(today_string)


date_string = '01/01/17 12:10:03.234567'

date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')

