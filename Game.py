secret = 43

guess = int(input("Guess the secret number (between 1 and 50): "))

if guess == secret:
    print("You got it the secret - Congrats!!")
else:
    print("You're wrong! Try again!")
