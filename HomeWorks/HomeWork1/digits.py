
#Student: Avichai Aziz
#Assignment no. 3
#Program: digits.py

#ex 3: Creating the character Z from numbers

num = input("Enter a 4-digit number: ")
n = int(num)    #convert to number
first_num = (n%10000//1000)
second_num = (n%1000//100)
third_num = (n%100//10)
last_num = n%10
if num == str(first_num) + str(second_num) + str(third_num) + str(last_num):
    print(last_num, third_num, second_num, first_num)
    print((" ")*5 + str(last_num))
    print((" ")*4 + str(third_num))
    print((" ")*3 + str(second_num))
    print((" ")*1 + str(first_num))
    print(first_num, second_num, third_num, last_num)
else:
    print("Error, close the program")
    
    




    








