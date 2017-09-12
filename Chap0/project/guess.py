import random

secret_number = random.randint(0,21)
print("Please take a guess at my number")
guess = int(input("> "))
for i in range(0,10):
    if guess < secret_number:
        print("Too small, try again.")
        print("Now you have " + str(9-i) + " chances left")
        print("Please take a guess at my number")
        guess = int(input("> "))
        i = i + 1
    elif guess > secret_number:
        print("Too big, try again.")
        print("Now you have " + str(9-i) + " chances left")
        print("Please take a guess at my number")
        guess = int(input("> "))
        i = i + 1
    elif guess == secret_number:
        print("good job!")
        break
