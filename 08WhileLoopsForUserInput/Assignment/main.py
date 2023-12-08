import random
number = random.randint(1, 10)
correct = True
lives_number = random.randint(1, 10)
lives_correct = True
lives = 3

print
while correct == False:
    print("Guess the random number:")
    checker = input()
    if checker in ("12345678910"):
        guess = int(checker)
        if guess == number:
            correct = True
        elif guess > number:
            print("Too High, Guess Lower")
        elif guess < number:
            print ("Too Low, Guess Higher")
    else:
        print("Please enter a valid number next time!")
print("Congratulations!")
print("")
print("Number Guesser With Lives:")

while lives_correct == False:
    print("Guess the random number:")
    lives_checker = input()
    if lives_checker in ("12345678910"):
        lives_guess = int(lives_checker)
        if lives_guess == lives_number:
            lives_correct = True
        elif lives_guess > lives_number:
            lives = lives - 1
            print("Too High, ",lives, "lives remaining")
        elif lives_guess < number:
            lives = lives - 1
            print("Too Low, ",lives, "lives remaining")
    elif lives > 0:
        print("Please enter a valid number next time!")
    elif lives == 0:
        lives_correct = True
        pass
print("Congratulations, you had ",lives, "lives remaining!")
amount = 50
while amount > 0:
    checker = input()
    if checker in ("25", "10", "5"):
        coin = int(checker)
        if coin ==