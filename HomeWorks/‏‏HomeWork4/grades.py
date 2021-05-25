
#Student: Avichai Aziz
#Assignment no.2
#Program: grades.py

#ex2:
#a. Name of the student with the highest average grade and its grade
#b. The grade (or grades) received most often 
#c. List of grades 0-100 not received at all

def checking_file_input(grades_file):
    '''checking if the grades file input is numbers'''
    for row in grades_file:
       split_row = row.split()
       for value in split_row:
           if not value.isdigit(): #if value is not a number
               return "error1"
   
def checking_file_input2(students_file):
    '''checking if the students file input is numbers and letters'''
    for row in students_file:
       split_row = row.split()
       for value in split_row:
           if not value.isdigit() and not value.isalpha(): #if value is not a number or letter
               return "error2"        

def students_file(students_file):
    '''creat dictionary of I.D(keys) and names(values) of the students'''
    dic1 = {}   #dictionary number 1 - include the Id and full names of the students
    for row in students_file:
        split_row = row.split()     #split between the id and the names
        dic1[split_row[0]] = " ".join(split_row[1:]) #add the keys and values to the dic
    return dic1

def grades_file(grades_file):
    '''creat dictionary of I.D(keys) and grades(values) of the students'''
    dic2 = {}
    for row in grades_file:
        split_row = row.split()     #split between the id and the grades
        dic2[split_row[0]] = " ".join(split_row[1:]) #add the keys and values to the dic
    return dic2

def average_grades(dic2):
    '''find the of average of each student'''
    list_averages = [] #list of all averages
    for key in dic2:
        split_values = dic2[key].split() #enter all the grades of each student to a list inside the dic
        average = sum([float(num) for num in split_values]) / len(split_values) #convert the grades to float and calculate the average grades
        list_averages.append(average)
    return list_averages

def list_ID(dic2):
    '''enter all the students ID's to a list'''
    list_ID = []
    for ID in dic2:
        list_ID.append(ID) #append each student ID to the list
    return list_ID
    
def Highest_Average_n_Name(dic1, list_averages, lst_ID):
    '''find the student with the highest average''' 
    Max_Average = max(list_averages) #the highest average grade
    Index_Max_Average = list_averages.index(Max_Average) #the index of the highest average grade in the list
    ID_highest_grade = lst_ID[Index_Max_Average] #the ID of the student with the highest average grade
    Student_name = dic1[ID_highest_grade] #find the name of the student in dic1 with his ID number
    return Student_name, Max_Average

def List_Grades(dic2):
    '''list of all the grades'''
    lst_grades = [float(grade) for key in dic2 for grade in dic2[key].split()]    
    return lst_grades

def Most_Often_Grade(lst_grades):
    '''count the numbers of time each grade appears and compare it to the list of grades with the same index
    change it to a set to avoid duplicates of grades and return it as a string'''
    list_counter = [lst_grades.count(num) for num in lst_grades] #contains the numbers of times each grade appears
    max_number = max(list_counter) #the max number in the list counter is the grade that apear most times
    Most_often_grades = set([lst_grades[i] for i in range(len(list_counter)) if max_number == list_counter[i]]) #set with the most often grades appears
    Most_often_grades_list = list(Most_often_grades) #change the set to a list
    str_lst_most = [str(grade_most) for grade_most in Most_often_grades_list] #convert the grades in the list to str
    return " ".join(str_lst_most) #return the grades as a string
        
def Grades_not_received(lst_grades):
    '''list of grades range from 0 to 100 that were not received at all''' 
    set_grades = set(lst_grades)
    set_numbers = set(i for i in range(0,101))
    grades_not_received = list(set_numbers - set_grades)
    return grades_not_received
    
file_students = open("students.txt", "r")
file_grades = open("grades.txt", "r")
check = checking_file_input(file_grades)
check2 = checking_file_input2(file_students)
if check != "error1" and check2 != "error2":    
    file_students = open("students.txt", "r")
    file_grades = open("grades.txt", "r")
    dic_names = students_file(file_students) #dictionary ID and names
    dic_grades = grades_file(file_grades) #dictionary ID and grades
    List_Averages = average_grades(dic_grades) #list of the averages of each student
    Lst_ID = list_ID(dic_grades) #list of the students ID's
    student_name, highest_average = Highest_Average_n_Name(dic_names, List_Averages, Lst_ID) #defines variables
    print(student_name, "have the highest average grade, with average of:", highest_average)
    Lst_grades = List_Grades(dic_grades) #list of all the grades
    print("The grades that appear the most are:", Most_Often_Grade(Lst_grades))
    print("The grades that not received from 0-100 are:\n{0}".format(Grades_not_received(Lst_grades)))
    file_students.close()
    file_grades.close()
else:
    if check == "error1":
        error = "error, invalid file values - enter only numbers!"
    elif check2 == "error2":
        error = "error, invalid file values - enter only numbers and letters!"
    print(error)  
  
file_students.close()
file_grades.close()