#TO get the current date time we use datetime library

from datetime import datetime

currentdate = datetime.now()
#now function returns the date time object

print('Today is :' + str(currentdate)+ '\n')
#end of first part of the code

#import timedelta function from datetime library

from datetime import timedelta
# or from datetime import datetime, timedelta

oneday = timedelta(days = 1)
twodays = timedelta(days = 2)
yesterday = currentdate - oneday
Day_before_Yesterday = currentdate - twodays
Tomorrow = currentdate + oneday
Day_after_tomorrow = currentdate + twodays

print('Yesterday was: '+ str(yesterday) + '\n')
print('Day before yesterday was : ' + str(Day_before_Yesterday) + '\n')
print('Tomorrow is : '+ str(Tomorrow) + '\n')
print('Day after tommor is : '+ str(Day_after_tomorrow) + '\n')

#use the date functions to control date formatting
print('\n Today Day: ' + str(currentdate.day) + '\n')
print('Hour : ' + str(currentdate.hour) + '\n')
print('Weekday : '+ str(currentdate.weekday()) + '\n')
print('Month : ' + str(currentdate.month) + '\n')
print('Year : ' + str(currentdate.year) + '\n')

#3rd part of the code get a date as a input and convert it to a string and display
from datetime import datetime , timedelta

birth_day = input('Enter your birth day (dd/mm/yyyy): ')
birthday_date = datetime.strptime(birth_day , '%d/%m/%Y')
print('Birth day is on: ', str(birthday_date))

one_day = timedelta(days =1)
day_before_Bday = birthday_date - one_day
print('Hii, Tomorrow is your birth day ! This is birth day evening : ' + str(day_before_Bday)+ '\n')

#create a checing if else loop to validate the users input
if birthday_date.day > 31 or birthday_date.day < 1:
    print('Erorr !!!\n' )
    print('You enter wrong day for your birth day !\n')
elif birthday_date.month > 12 or birthday_date.month < 1:
    print('Erorr !!!\n')
    print('You entered wrong month for your birth day! \n')
elif birthday_date.year < 1900 or birthday_date.year > 2024:
    print('Erorr !!!\n')
    print('You entered wrong year as your birth day !\n')
else:
    print('Hello Sire, ' + str(birthday_date) + ' is your birth day !, May i wish on that day?\n')            