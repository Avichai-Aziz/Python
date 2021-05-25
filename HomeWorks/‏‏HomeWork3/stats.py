
#Student: Avichai Aziz
#Assignment no. 1
#Program: stats.py

#ex1: print the average,max and min num, its indexes and if the series rising,goes down or have no order of a series numbers

def string_to_list(lst):
    #turning a string of series numbers to list of floating numbers, return list
    list1 = []  #a new list
    for number in lst: #goes over all the string numbers
        if number.isdigit():    #checking if its positives numbers
            number = float(number)    #change the string numbers to a float
            list1.append(number)    #append the float numbers to a list
        elif number[0] == "-":  #chcking if its negative numbers
            number = float(number)    #change the string numbers to a float
            list1.append(number)    #append the float numbers to a list
        else:   #if isnt numbers
            print("series entered incorrectly")
            return None 
    return list1    #return list of integer numbers

def average_of_list_numbers(lst):
    #calculate the average of series numbers, return the average
    total = 0
    for number in lst: #goes all over the numbers inthe list
        total += number     #calculate the sum of the series numbers
    average = total/len(lst) #the average of the series numbers
    return average

def maxNumber(lst):
    #finding the maximum number in the series
    max_num = max(lst)    #finding the max number in the series
    return max_num

def index_max_number(lst):
    #finding the index of the maximum number in the series
    max_num = max(lst)    #finding the max number in the series
    index_max_num = lst.index(max_num) +1     #finding the max number index add 1 to start the index series from 1
    return index_max_num

def minNumber(lst):
    #finding the minimum number and its index
    min_num = min(lst)    #finding the min number in the series
    return min_num

def index_min_number(lst):
    #finding the minimum number and its index
    min_num = min(lst)    #finding the min number in the series
    index_min_num = lst.index(min_num) +1     #finding the min number index add 1 to start the index series from 1
    return index_min_num

def find_rising_series(lst):
    #check if the series numbers rising
    first_num = lst[0]
    for i in range(1,len(lst)):
        second_num = lst[i]
        if first_num < second_num: #compare one number with the other
            first_num = second_num
        else:   #if the series isnt rise, it maybe goes down, therefor we need to check it
            return find_series_goes_down(lst)
    rise = "the series is rising"
    return rise

def find_series_goes_down(lst):
    #check if the series numbers goes down
    first_num = lst[0]
    for i in range(1,len(lst)):
        second_num = lst[i]
        if first_num > second_num: #compare one number with the other
            first_num = second_num
        else:  #if the series is'nt rise and is'nt goes down, its have no order
            no_order = "the series have no order" 
            return no_order
    goes_down = "the series goes down"
    return goes_down   

lst_string = input("enter a series numbers: ").split()
list2 = string_to_list(lst_string)
if list2 != None:   #checking the input 
    print("the average is:",average_of_list_numbers(list2))
    print("the max num is: {0}".format(maxNumber(list2)), "in place: {0}".format(index_max_number(list2)))
    print("the min num is: {0}".format(minNumber(list2)), "in place: {0}".format(index_min_number(list2)))
    print(find_rising_series(list2))
else:   #if the input is not currect
    print(list2)