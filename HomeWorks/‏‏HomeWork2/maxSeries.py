
#Student: Avichai Aziz
#Assignment no. 1
#Program: maxSeries.py

#ex 1: finding the avarege of series numbers, max and min and the index, to stop press 0

#define variables
list_num = []
num = 1
avarege_of_series = 0
sum_numbers = 0
while num != 0:
    #enter a series of integer numbers, press 0 to stop    
    num = int(input("enter a integer: "))        
    list_num.append(num)    #entering numbers into the list
new_list = list_num[:-1]    #list without number 0
for i in (new_list):
    numbers = len(new_list)     #the amount of numbers in the series
    sum_numbers += i    #the sum of numbers in the series
avarege_of_series = (sum_numbers) / (numbers)
max_num = max(new_list)     #the max number in the series
min_num = min(new_list)     #the min number in the series
index_max = ((new_list.index(max(new_list))) + 1) #index starts at 0,so need to add 1
index_min = ((new_list.index(min(new_list))) + 1) #index starts at 0,so need to add 1
print("the avarege of series is:", avarege_of_series)
print("the max value is:", max_num, ",in cell:", index_max)
print("the min value is:", min_num, ",in cell:", index_min)
