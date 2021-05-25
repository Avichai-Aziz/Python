
#Student: Avichai Aziz
#Assignment no. 3
#Program: dice3.py

#ex 3: rolling three dice

import random
#define variables
n = int(input("Enter the number of games: "))
k = int(input("Enter the number of equal series: "))
n_game = 0  #number of game
equal_series = 0   #numbers of equal series
n_of_tries = 0 #numbers of tries
while n_game <= n and k <= n:
    for n_game in range(1,n+1):
            #dropping the dice
        dice1 = random.randint(1, 6)    #first cube
        dice2 = random.randint(1, 6)    #second cube
        dice3 = random.randint(1, 6)    #third cube
        print(dice1, ',', dice2, ',', dice3)
        if dice1 == dice2 == dice3:     #if the dice are equals
            equal_series += 1           #add 1 to the equal series
            n_of_tries = n_game
    if n_game == n and equal_series < k:
            print("you failed,reached", equal_series, "equal series")
            break
    elif equal_series >= k and n_game == n:
        print("you win! reached", equal_series, "equal series after", n_of_tries, "games")
        break
else:   #if the user input number of equal series that bigger than the numbers of games or negative numbers
    print("error, try again")   
