import calendar

yy = 1996
mm = 7
print(calendar.month(yy, mm))

print(calendar.calendar(1996))

if  calendar.isleap(2000):
    print("The year is leap year")
else:
   print("The year is not leap year") 

c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(1996, 7)
print(str)

hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(1996, 7)
print(str)