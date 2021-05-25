
#Student: Avichai Aziz
#Assignment no. 2
#Program: calendar.py

#ex2: print a calendar of month in a year

def split_month_and_year(year_month):
    #split the input string to year and month
    for value in year_month: 
        if value.isalpha(): #check if the value is letters
            month = value #the input month
        elif value.isdigit(): #check if the value is numbers
            year = int(value) #the input year (as an integer)
    return year, month

def months_in_year(month):
    #return the input month of the year with capital letter, So it willn't be a problem with uppercase or lowercase letters
    month = month.lower() 
    month = month.capitalize()
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    if month in months:
        return month
    else: #if the month or isnt entered currectly
        error = "month or year has not been entered correctly"
        return error

def leap_year(year):
    #check if leap year
     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):   
         leap_year = True
         return leap_year
     else:  #if it regular year
         leap_year = False
         return leap_year

def numbers_of_days_in_month(year):
    #number of days in regulr year and leap year
    month = months_in_year(month1)
    leap_year1 = leap_year(year) #value of leap year- True\False
    months = {"January":31,"February":28, "March":31, "April":30, "May":31,
              "June":30, "July":31,"August":31, "September":30, "October":31, 
              "November":30, "December":31} 
    if leap_year1 == True: #if its leap year
        months["February"] = 29 #in leap year "February" month have 29 days
        number_of_days = months[month] #number of days in each month
        return number_of_days                    
    else: #if its regular year
        number_of_days = months[month] #number of days in each month
        return number_of_days 

def days_of_week():
    #return the first letters of the days on a week
    days_week = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"] #first letters of the days in the week
    days_week = "  ".join(days_week) #change the list of days in the week to a string
    return days_week 

def sum_of_days_in_months(month,year):
    #calculet the sum of the days in all years by counting the days of each month
    month = months_in_year(month)
    sum_days_in_month = 0
    months = ["January","February", "March", "April", "May","June", "July",
              "August", "September", "October", "November", "December"]
    for each_year in range(1900,year+1): #goes all over the years, from 1900 to the requsted year+1 (to include it)
        leap_year1 = leap_year(each_year) #check each year if it leap or regular
        days_months = [31,28,31,30,31,30,31,31,30,31,30,31]
        
        if leap_year1 == True:
            days_months = [31,29,31,30,31,30,31,31,30,31,30,31]
            if each_year == year: #to count the specific year until the month(not include the month)
                for i in range(months.index(month)):
                    sum_days_in_month += days_months[i] #sum the days total
            else:
                for i in range(len(days_months)): #count the days of each month
                    sum_days_in_month += days_months[i]
        
        if leap_year1 == False:
            if each_year == year:
                for i in range(months.index(month)):
                    sum_days_in_month += days_months[i]
            else:
                 for i in range(len(days_months)):
                     sum_days_in_month += days_months[i]             
    return sum_days_in_month

def calculator_days(month, year):  
    #calculat the day of the first in the month
    sum_days_months = sum_of_days_in_months(month1, year1)
    sum1 = sum_days_months +2 #add 2 beacuse the first in january 1900 is Monday
    the_day_of_the_first = sum1 % 7 #modulo 7 becuse there is 7 days a week
    return the_day_of_the_first

def calender(month, year):
    #print calender of month in year
    months_in_year(month) #the month input
    number = numbers_of_days_in_month(year) #numbers of days each month
    the_day_of_the_first = calculator_days(month, year)
    counter_days = the_day_of_the_first
    if counter_days != 0:
        counter_days = the_day_of_the_first-1     #counter days, to down a row, -1 becuase there is 1 to much tab space    
    print(days_of_week())   #print the days in the week
    print("{0:<4}".format("")*(the_day_of_the_first-1), end="") #print the tab space according to the day is the first for month -1   
    for days in range(1,number+1): #goes all over the numbers of days in the requested month, start from 1
        print("{0:<4}".format(days), end="") #print each day
        counter_days += 1 #add 1 to the counter days     
        if counter_days == 7: #to know when down a row
            print()
            counter_days = 0 #reset the counter if arrive to 7 and get down a row    
    return "\b"

year_month1 = input("enter a month and a year: ").split()
year1, month1 = split_month_and_year(year_month1)
print(calender(month1, year1))
