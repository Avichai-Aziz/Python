
#Student: Avichai Aziz
#Assignment no. 3
#Program: matrix.py

#ex3: printing the multiply of two matrixes A'*B

def matrixFile_to_list(lst):
    #turning a file that containing matrixes to a lists
    inner_list_A = []   #list of matrix A
    inner_list_B = []   #list of matrix B
    for values in lst:  
        if values == "A=":  #enter the matrix A to a list
            for i in range(1,len(lst)):     #goes all over the indexes in the string list
                for j in range(1,len(values)): #goes all over the indexes of each value in the list
                    if lst[i][j] != "B=":   #checking where to start and stop the list of matrix A
                        if lst[i] != "B=":
                            couple_numbers = lst[i].split() #split each row of matrix A to a list
                            inner_list_A.append(couple_numbers) #append each row to inner list that uniting all the rows in matrix A
                    if lst[i] == "B=": #checking where to start matrix B list
                        for k in range(i+1,len(lst)): #goes all over the indexes of matrix B
                            couple_numbers = lst[k].split() #split each row of matrix B
                            inner_list_B.append(couple_numbers) #append each row to inner list that uniting alll the rows in matrix A
                            if k == len(lst)-1: #checking the last index to stop adding numbers to matrix B list
                                return inner_list_A, inner_list_B

def stringList_to_numberList(lst):
    #turning string numbers in list to float numbers in list, retur 2 lists A and B 
    out_list = matrixFile_to_list(lst) 
    inner_list_A = []
    inner_list_B = []
    list_A_out = []
    list_B_out = []
    for i in range(len(out_list)-1): #goes all over the indexes of matrix A
        for list1 in out_list[i]: #goes all over the lists in list matrix A
            for j in range(len(list1)): #goes all over the indexes of each list in the matrix A list
                num = float(list1[j]) #change the numbers in the list to float
                inner_list_A.append(num) 
            list_A_out.append(inner_list_A)
            inner_list_A = []
    for i in range(1,len(out_list)): #goes all over the indexes of matrix B
        for list1 in out_list[i]: #goes all over the lists in list matrix B
            for j in range(len(list1)): #goes all over the indexes of each list in the matrix B list
                num = float(list1[j]) #change the numbers in the list to float
                inner_list_B.append(num) 
            list_B_out.append(inner_list_B)
            inner_list_B = []        
    return list_A_out, list_B_out

#a. return the replaced matrix (2 options: with loops, or with list comprehension)
#option 1: with loops
def row_to_col(matrix): 
    #change the columns of the matrix to the rows, return matrix
    list1 = [] #a new list
    for col in range(len(matrix[0])): #pass all over the columns in the matrix
        list2 = [] #inner list
        for row in range(len(matrix)): #pass all over the rows in the matrix
            number = matrix[row][col]            
            list2.append(number)
        list1.append(list2) 
    return list1

#option 2: with list comprehension
def row_to_col_2(matrix):
    #change the columns of the matrix to the rows, return matrix
    return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]
#b. return the multiply of two matrixes A,B
def matrix_mult(m1,m2):
    #multiply the two matrix, return a new matrix
    if len(m1[0]) == len(m2):   #checking if the columns in matrix 1 equal to the rows in matrix 2
        lst = []    #a new list
        for row in range(len(m1)): #pass all over the rows in the matrix
            lst2 = []   #inner list
            for col in range(len(m2[0])): #pass all over the columns in the matrix
                sum1 = 0    #reset the sum of multiply row in column to zero every column
                for i in range(len(m1[0])): 
                    sum1 += m1[row][i] * m2[i][col] #multiply the every row and column and sum them
                lst2.append(sum1) #append the sum to the inner list
            lst.append(lst2) #append the inner list to the outside list
        return lst 
    else:
        error = "matrix entered incorrectly"
        return error

#c.print each row sepertly
def print_matrix(matrix):
    #print each row in the matrix separately    
    for row in range(len(matrix)):
        print("|",end=" ") #print the border lines
        for col in range(len(matrix)):
            num = matrix[row][col]
            print("{:.1f}".format(num),end=" ") #print the numbers and  1 number after the point
        print("|") #print the border lines
    return "\b"

#main program:
file = open("matrices.txt","r")
text = file.read().split(" ")
text = " ".join(text)
lst_text = text.splitlines()
file.close()
matrixFile_to_list(lst_text)
A ,B = stringList_to_numberList(lst_text)
inverse_A = row_to_col(A) #option 1: with loops
inverse_A = row_to_col_2(A) #option 2: with list comprehension
AB = matrix_mult(inverse_A,B) #multiply function
print_matrix(AB)







