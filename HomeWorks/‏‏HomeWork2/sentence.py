
#Student: Avichai Aziz
#Assignment no. 5
#Program: Sentence.py

#ex 5: Writing a sentence in a column and checking the number of words in it 

#write a sentence
sentence = input("enter a sentence: ")
#define variables
inword = False
counter = 0     #count the number of words
for i in sentence:  #passes every letter or interval in the sentence
    if not i.isspace():     #checking if "i" is a interval
        print(i, end="")    #printing the characters
        if inword == False: #checking if the string before were a word\interval
            inword = True   #is in the word
            counter += 1
    else:
        inword = False  #is not in the word
        i = print()     #print a new line instead of a interval
print()
print("There are", counter, "words in:", sentence)
