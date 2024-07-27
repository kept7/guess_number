import random

name = input("Hello! What is your name? \n") 
print ("Well, ", name,", I'am thinking of a number between 1 and 25. Take a guess.", sep='') 

num = random.randint(1, 25)
tries = 0

while tries < 6:
    x = input()
    x = int(x)
    tries += 1 
    if x > num:
        print('Your guess is to high. Try number a bit lower.')
    elif x < num:
        print('Your guess is to low. Try number a bit higher.')
    if x == num: 
        print("Good job, ", name, ", you guessed my number. The guessed number was ", num, " and you guessed it on ", tries, " try.", sep='')
        break

if x != num:
    print ("You've used up all your attempts, try again.")