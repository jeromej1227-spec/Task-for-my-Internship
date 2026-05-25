import datetime
name=input("Enter your Name:")
age=int(input("Enter your Age:"))
y=datetime.datetime.now()
year=int(y.strftime("%Y"))
n=60-age
a=year+n
if n>0:
    print(name,", your age will turn into 60 in",a)
else:
    print(name,", you crossed age 60 in",a)