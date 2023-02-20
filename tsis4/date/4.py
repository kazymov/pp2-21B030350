import datetime 

x1=datetime.datetime(2023,2,21)
x2=datetime.datetime(2022,2,22)

res=(x1-x2).total_seconds()
print(res)