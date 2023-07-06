import random

while True:
    
    turns_left = 8
    
    print("Welcome to Mastermind!\nYou have", turns_left, "turns to try and guess the secret number (between 100 and 999)!")

    secret = str(random.randint(100, 999))
    
    while turns_left > 0:
        white_peg = 0
        black_peg = 0
        
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
                black_peg += 1
            else:
                guess_list.append(g)
                secret_list.append(s)
            
        for g in guess_list:
            if g in secret_list:
                white_peg += 1
                secret_list.remove(g)
                
        print("That guess got", black_peg, "black pegs and", max(white_peg, 0), "white pegs \n")
        turns_left -= 1
        
    if turns_left == 0:   
        print("Good try! The secret number was", secret)
        
    finish = input("Play again? [y/n]:").lower()
    if finish != 'y':
        break
