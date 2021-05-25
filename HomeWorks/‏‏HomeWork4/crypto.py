
#Student: Avichai Aziz
#Assignment no.1
#Program: crypto.py

#ex1:
#a.creat a key ("k")
#b.encrypt ("e")
#c.decrypt ("d")
#d.another letter-stop programe

import random

def Key(letters):
    '''creat a random encrypt key, and write it to a text file'''
    list_key = [] #list of the keys
    counter_letters = 0 #count the letters
    while counter_letters < 26:
        letter = random.choice(letters) #pick a random letter from letters
        if letter not in list_key: #checks no duplicates of letters
            list_key.append(letter) #append the letter if it is not appear in the list
            counter_letters += 1 
    key_str = "".join(list_key) #convert the list to a string
    return key_str
 

def dictionary(letters):
    '''dic- the letters a-z is keys and the values are the "keys encrypt" 
    from the key.txt file'''
    dic = {}
    file_key = open("key.txt", "r")
    read_key_file = file_key.read()
    file_key.close()
    for i in range(len(letters)):
        dic[letters[i]] = read_key_file[i] #add keys(letters a-z) and values(keys encrypt)
    return dic


def Encrypt(dic_val_keys, plaintext_read):
    '''append the values of the file to a list, lower them-if letters,
    and return encrypt letter string.'''
    lst_encrypt = [value.lower() for value in plaintext_read] #list with all the letters from the plaintext file
    i = 0   #used as a counter and index
    while i < len(lst_encrypt):
        if lst_encrypt[i].isalpha(): #checking if value is letter
            lst_encrypt[i] = dic_val_keys[lst_encrypt[i]] #encrypt the letter to a encrypt key letter
            i += 1 #add 1 to continue to the next value
        elif lst_encrypt[i].isspace() or lst_encrypt[i] == "\n": #checking if the value is space or a linebreak
            i += 1
            continue
        else:
            lst_encrypt.pop(i) #remove the values who isn't english letters,space or linebreak from the list
    str_encrypt = "".join(lst_encrypt) 
    return str_encrypt          
 

def dictionary2(letters, key_read):
    '''dic2- the "keys encrypt" from the key.txt file are keys and the letters a-z the values'''
    dic2 = {}
    for j in range(len(key_read)):
        dic2[key_read[j]] = letters[j] #add keys(keys encrypt) and values(letters a-z)
    return dic2


def Decrypt(ciphertext_read, dic_val_a_z):
    '''decrypt the the encrypt letters'''
    lst_Decrypt = [] #list of the decrypted letters
    for value in ciphertext_read:
        if value.isalpha(): #check if the value is letter
            lst_Decrypt.append(dic_val_a_z[value]) #append the decrypted letter
        elif value.isspace() or value == "\n": #check if the valye is space or a linebreak
            lst_Decrypt.append(value) 
        else:
            continue
    str_Decrypt = "".join(lst_Decrypt) #convert the list to a string of decrypted letters
    return str_Decrypt

#main programe:
Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
           'r','s','t','u','v','w','x','y','z']
while True:
    input1 = input("select an action: k-key, e-encrypt, d-decrypt, exit-any other value: ")
    if input1 == "k" or input1 == "e" or input1 == "d":
        if input1 == "k": #Key
           Key_str = Key(Letters) #the key letters as a string
           file_key = open("key.txt","w")
           file_key.write(Key_str) #write into key file
           file_key.close()
        Dic_val_Keys = dictionary(Letters) #dictionary- keys are letters (a-z), values are the keys letters

        if input1 == "e": #Encrypt
            file_plaintext = open("plaintext.txt", "r")
            file_plaintext_read = file_plaintext.read() #read from plaintext file
            Str_encrypt = Encrypt(Dic_val_Keys ,file_plaintext_read) #encrypt string letters
            file_plaintext.close()
            file_ciphertext = open("ciphertext.txt", "w")
            file_ciphertext.write(Str_encrypt) #write into ciphertext file
            file_ciphertext.close()

        if input1 == "d": #Decrypt
             file_key = open("key.txt","r")
             file_key_read = file_key.read() #read from key file
             file_ciphertext = open("ciphertext.txt", "r")
             file_ciphertext_read = file_ciphertext.read() #read from ciphertext file
             Dic_val_A_z = dictionary2(Letters, file_key_read) #dic with keys letters as keys and letters a-z as a values
             Str_decrypt = Decrypt(file_ciphertext_read, Dic_val_A_z) #letters of the decrypt as a string
             file_decrypted = open("decrypted.txt", "w")
             file_decrypted.write(Str_decrypt) #write into decrypted file
             file_decrypted.close()
             file_ciphertext.close()
             file_key.close()

    else: #if the user input another value -end programe
        break       