# Mohammad Qureshi
# PSID 1789301
# Homework Problem 1


from datetime import date

# INPUT CURRENT DATE
print('Enter the current date')
curr_month = int(input('Month:'))
curr_day = int(input('Day:'))
curr_year = int(input('Year:'))

#INPUT BIRTHDAY
print('Enter Birthday Month')
birth_month = int(input('Month:'))
birth_day = int(input('Day:'))
birth_year = int(input('Year:'))


# CALCULATE AGE
year = curr_year - birth_year
if(birth_month > curr_month):
    print(year)
elif(birth_month < curr_month):
    print(year - 1)
else:
    if(birth_day >= curr_day):
        print(year)
    else:
        print(year-1)


# PRINT HAPPY BIRTHDAY
if((birth_month == curr_month) & (birth_day == curr_day)):
    print('Happy Birthday!')