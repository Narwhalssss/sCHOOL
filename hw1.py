
import random
rndmNum = random.randint(0,100)

urGuess = "..."
urGuess = int(input(print('pick a number between 1 - 100 ')))

while urGuess != rndmNum:
    if urGuess > rndmNum:
        print("lower")
        urGuess = int(input(print('pick a number between 1 - 100 ')))
    elif urGuess < rndmNum:
        print("higher")
        urGuess = int(input(print('pick a number between 1 - 100 ')))
    else:
        print("YEESSSSSSSSSS")
        