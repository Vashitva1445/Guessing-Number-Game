import random
n=random.randint(1,100)

while True:

    guess=int(input("Guess a number between 1 and 100: "))
    if guess==n:
        print("You guessed it!!")
        break;
    elif guess>n:
        print("Too big!!")
    else:
        print("Too small!!")

