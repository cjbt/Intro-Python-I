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
from datetime import datetime

x = input("14_cal.py month [year]").split(',')
calendar.setfirstweekday(0)
cal = calendar.Calendar()


def makeCal(*args):
    if len(args) > 1:
        for x in cal.itermonthdays(int(args[1]), int(args[0])):
            print(x)
    elif len(args) == 1 and args[0] != '':
        for x in cal.itermonthdays(2019, int(args[0])):
            print(x)
    elif args[0] == '':
        print(str(datetime.today())[5:7])
    print('must take in a month and a date separated by commas: month,year')
    sys.exit()


# class calendar.Calendar(6)


# print(cal(*x))
print(makeCal(*x))
