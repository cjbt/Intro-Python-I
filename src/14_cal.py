"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
import datetime

calendar.setfirstweekday(0)
cal = calendar.Calendar()


def makeCal(*args):
    year = int(str(datetime.datetime.today())[:4])
    month = int(str(datetime.datetime.today())[5:7])
    if len(args) > 1:
        print(calendar.TextCalendar(firstweekday=0).formatmonth(
            int(args[1]), int(args[0])))
    elif len(args) == 1 and args[0] != '':
        print(calendar.TextCalendar(firstweekday=0).formatmonth(
            year, args[0]))
    elif args[0] == '':
        print(calendar.TextCalendar(firstweekday=0).formatmonth(
            year, month))
    print('must take in a month and a date separated by commas: month,year')
    sys.exit()


print(makeCal(*sys.argv[1:]))
