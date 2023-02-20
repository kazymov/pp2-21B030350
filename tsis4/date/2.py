import datetime

x=datetime.datetime.now()
x1=x-datetime.timedelta(days=1)
x2=x+datetime.timedelta(days=1)
print(f"now: {x.strftime('%d')}")
print(f"yesterday: {x1.strftime('%d')}")
print(f"tomorrow: {x2.strftime('%d')}")