import calendar
# c=calendar.Calendar(0)
# c.setfirstweekday(2)
# c.setfirstweekday(0)
# for i in c.iterweekdays():
#     print(i)
# for i in c.itermonthdays(2020, 12):
#     print(i,end="    ")
# print("\n__________________")
# for j in range(12):
#     for i in c.itermonthdates(2020, 1):
#         print(i,end="\t")
#     print("__________________________________")
# mylist=list()
# for i in c.itermonthdays2(2023, 1):
#     print(i,end='   ')
#     mylist.append(i)
#     #appending a list with the tuples of day number and WeekDay number of the month'1', then printing this list
# print("__________________________________")
# for i in mylist:
#     print(i,end=',')
#     print(type(i),end='    ')
# print("__________________________________")
# a=c.monthdatescalendar(2023,1)#list of the weeks in the month month of the year as full weeks is returned 
# for i in a:
#     print(i)
# b=c.monthdays2calendar(2023, 1)#returns a list of list of weeks in a month,each list contain a tuplpe of day number and week day number in that month
# for i in b:
#     print(i)
# d=c.monthdayscalendar(2023, 1)#return day numbers of the week of the month
# print(d)

# c2=calendar.TextCalendar()
# print(c2)## will not show any thinf but memory addesss
# print(c2.formatmonth(2023, 1))
# print(c2.formatyear(2023,5))#secondn peremeter is the width which is the spacing between the columns of each month

# c3=calendar.HTMLCalendar()
#these will return calendar as html codes
# print(c3.formatmonth(2023,1,True))
# print(c3.formatyear(2023))
# print(c3.formatyearpage(2023))

# c4 =calendar.weekday(2023, 12, 1)
# c4 =calendar.monthcalendar(2023, 12)
# c4=calendar.TUESDAY#this will return the weekday number
#  c4=calendar.January#this will return the month number
# print(c4)