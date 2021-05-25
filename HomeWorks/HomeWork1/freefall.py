
#Student: Avichai Aziz
#Assignment no. 1
#Program: freefall.py

#ex 1: finding the time and speed of a stone from a freefall

high = input("Enter the height of the stone throw (m): ")   #measured in meters
h = float(high)     #convert to number
g = 9.8     #the constant free fall (m/sec**2)
import math
time = math.sqrt(((2*h)/9.8))   #measured in (m/sec)
velocity = g * time     #measured in (m/sec)
print("it will take",time, "sec,to touch the ground,and the speed stone would be", velocity ,"m/sec")



