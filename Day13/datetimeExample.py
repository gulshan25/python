import datetime

datetime_obj=datetime.datetime.now()
print(datetime_obj)

datetime_obj=datetime.date.today()
print(datetime_obj)

from datetime import datetime,date
datetime_obj=datetime.now()
print(datetime_obj)

datetime_obj=date.today()
print(datetime_obj)

# datetime_obj=time.today()
# print(datetime_obj)

cdate=datetime.now()
print(cdate)
print(cdate.year)
print(cdate.month)
print(cdate.day)

print(cdate.hour)
print(cdate.minute)
print(cdate.second)
print(cdate.microsecond)

# week day 

print(cdate.strftime('%a'))
print(cdate.strftime('%A'))
print(cdate.strftime('%w'))

# Month

print(cdate.strftime('%b'))
print(cdate.strftime('%B'))
print(cdate.strftime('%m'))

# day

print(cdate.strftime('%d'))
# Y for year
print(cdate.strftime('%y'))  
print(cdate.strftime('%Y'))  

# Time

print(cdate.strftime('%H'))
print(cdate.strftime('%I'))
print(cdate.strftime('%p'))
print(cdate.strftime('%M'))
print(cdate.strftime('%S'))
print(cdate.strftime('%f'))
print('-'*50)
# Custom formatting
print(cdate.strftime('%d-%m-%Y'))
print(cdate.strftime('%A, %m/%d/%Y'))
print(cdate.strftime('%H:%M:%S'))
print(cdate.strftime('%I:%M:%S %p'))
