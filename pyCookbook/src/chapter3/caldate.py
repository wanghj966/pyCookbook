import datetime
today=datetime.date.today()
yesterday=today-datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1)
print today,yesterday,tomorrow