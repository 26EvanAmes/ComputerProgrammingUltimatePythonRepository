import random
number = random.randint(1, 10)
correct = False
lives_number = random.randint(1, 10)
lives_correct = False
lives = 3

print
while correct == False:
    print("Guess the random number:")
    checker = input()
    if checker in ("12345678910") and checker != "":
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
    if lives_checker in "12345678910" and lives_checker != "" and lives > 0:
        lives_guess = int(lives_checker)
        if lives_guess == lives_number:
            lives_correct = True
            pass
        elif lives_guess > lives_number:
            lives = lives - 1
            print("Too High, ",lives, "lives remaining")
            pass
        elif lives_guess < lives_number:
            lives = lives - 1
            print("Too Low, ",lives, "lives remaining")
            pass
    elif lives > 0:
        print("Please enter a valid number next time!")
    elif lives < 1:
        lives_correct = True
        pass
    else:
        print("error")
if lives == 0:
    print("So close, you had ",lives, "lives remaining!")
if lives > 0:
    print("Congratulations, you had ",lives, "lives remaining!")
amount = 50
while amount > 0:
    print("Amount due:", amount)
    print("Please enter a valid coin")
    checker = input()
    if checker in ("25", "10", "5"):
        coin = int(checker)
        if coin == 25 and amount >= 25:
            amount = amount - 25
        if coin == 10 and amount >= 10:
            amount = amount - 10
        if coin == 5 and amount >= 5:
            amount = amount - 5
    else:
        print("Please enter a valid coin next time")
print("Snack successfully purchased")


