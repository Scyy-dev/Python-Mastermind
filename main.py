import random

while True:

    turns_left = 8

    print("Welcome to Mastermind!\nYou have", turns_left,
          "turns to try and guess the secret number (between 100 and 999)!")

    secret = str(random.randint(100, 999))

    while turns_left > 0:
        number_correct = 0
        position_correct = 0

        guess = input("Guess a number:")
        while len(guess) != 3:
            print("Too small! Must be 100-999")
            guess = input("Guess a number: ")

        if guess == secret:
            print("You got it!")
            break

        guess_list = []
        secret_list = []

        for g, s in zip(guess, secret):
            if g == s:
                position_correct += 1
            else:
                guess_list.append(g)
                secret_list.append(s)

        for g in guess_list:
            if g in secret_list:
                number_correct += 1
                secret_list.remove(g)

        print("That guess got", position_correct, "numbers in the right position and", number_correct,
              "other correct numbers.")
        turns_left -= 1

    if turns_left == 0:
        print("Good try! The secret number was", secret)

    finish = input("Play again? [y/n]:").lower()
    if finish != 'y':
        break
