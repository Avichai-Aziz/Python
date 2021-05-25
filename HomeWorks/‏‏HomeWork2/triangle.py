
#Student: Avichai Aziz
#Assignment no. 4
#Program: triangle.py

#ex 4: triangle with dolars and spaces inside

#setting variables
height = int(input("enter the height of the triangle: "))
#the minimum height of the triangle is 2
if height > 1:
    n_dolars = int(input("enter the number of dolars: "))
    space_input = int(input("enter the number of spaces: ")) #the input spaces between each group of dollars
    space_str = " " 
    star = "*"
    dolar = "$"
    base = ((height*2)-1)   #the base of the triangle
    triangle_area = (base) * (height)   #the triangle area
    string_dolars = (n_dolars) * (dolar)
    string_spaces = (space_input) * (space_str)
    string_d_s = (string_dolars + string_spaces) * (triangle_area) #the string of dolars and spaces inside the triangle
    index_string_d_s = 0    #the index of the dolars and space string
    counter_lines = 0       #count the number of the lines
    for row in range(1,height):         #the lines
        for column in range(1,base+1):  #the columns
            if (column) < (height - counter_lines): 
               print(space_str , end="")      #the outside left rib of the triangle
            elif (column-row) > (height-1):
               print(space_str , end="")      #the outside right rib of the triangle                
            elif (column-row) == (height-1):
                print(star, end="")     #the right rib of the triangle
            elif ((column-row) + counter_lines) == ((height-1) - counter_lines):
                print(star, end="")     #the left rib of the triangle
            else:
                print(string_d_s[index_string_d_s], end="") #print the dolars and spaces inside the triangle
                index_string_d_s += 1 #adds 1 to promote the index in the string of dollars and spaces
        counter_lines += 1  #adds 1 to the counter lines after each line has ended   
        print()     #down a line after each line ending       
    print((star) * ((height * 2)-1))    #the base of the triangle
#if the user enter a height lower than 2
else:   
    print("Error,try again")
    print("the minimum height of the traingle is 2")
