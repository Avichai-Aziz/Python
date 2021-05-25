
#Student: Avichai Aziz
#Assignment no. 2
#Program: decSeries.py

#ex 2: The longest descending series length

N = 10          #the numbers in the whole series
count_N = 1   #count the numbers in the whole series
counter = 1   #count the numbers of each series
N_biggest = 1 #numbers in the biggest descending series
num = float(input("enter a number: "))    
for count_N in range(1, N):
    num2 = float(input("enter the next number: "))
    if num > num2:
        counter += 1    #add 1 to the counter of each series
        if counter >= N_biggest:
            N_biggest = counter
    elif num <= num2:
        counter = 1     #start to re-count the next series
    num = num2
    count_N += 1    #add 1 to the counter of the whole series
print("The length of the longest descending series is", N_biggest, "numbers")
