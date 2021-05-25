
#Student: Avichai Aziz
#Assignment no. 4
#Program: quadratic.py

#ex 4:Coefficients of a quadratic equation

first_parameter = input("Enter first parameter (a): ")
second_parameter = input("Enter second parameter (b): ")
third_parameter = input("Enter third parameter (c): ")
a = int(first_parameter)
b = int(second_parameter)
c = int(third_parameter)
from math import sqrt
y = (b **2) - (4 * a  * c)  #the value inside the square root
if y < 0:
    print("no solution")
elif y > 0:
    sqrt = sqrt(y)
    x1 = (-b + sqrt)/2
    x2 = (-b - sqrt)/2
    print("two solutions:",x1, ",", x2)
else:
    sqrt = sqrt(y)
    x1 = (-b + sqrt)/2
    x2 = (-b - sqrt)/2
    print("one solution:", x1 or x2)
    
    
    







    








