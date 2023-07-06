# Objective

The goal of this project is to create a digital version of
the [Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game)) game. We'll be writing it in Python and
simplifying it to make it easier for us to implement and understand.

# Line-by-line Explanation

### Needed Libraries

The first thing we need is the `random` library to generate our secret random number.

```python
import random
```

### Core Game Loop

Before we start our game, we need to create a way for our player to play again as many times as they like. This is
what's known as the 'core game loop', and it makes it much easier for our player to play again and again.

To do this, we create an infinite loop, and add a prompt to escape from the loop. The prompt asks for a yes/no response,
and we can check what the answer is by looking for a 'y' - if they made a typo or said no, we'll assume they want to
quit.

```python
while True:

    # Our gameplay will go here! We'll be writing all our code here after this.

    finish = input("Play again? [y/n]: ").lower()
    if finish == 'y':
        break
```

Now that we've got our loop set up, it's time to create our game!

### A Number Guesser?

The core of our game revolves around players guessing a number.We give them a set number of turns to try and guess.
During the guessing part of the game, the player guesses a number. If they get it right, we celebrate! If they get it
wrong, we give them clues based on the number of correct numbers they got, and if they're in the right order. If they
run out of guesses, we'll give them the correct answer.

An example game could look like this:

```
Welcome to Mastermind!

Guess a number: 123
That guess got 1 number in the right position and 0 other correct numbers.

Guess a number: 345
That guess got 1 number in the right position and 2 other correct numbers.

Guess a number: 543
You got it!
Play again? [y/n] n
```

That's a lot to take in! We'll break this down step-by-step and see what we need to code in.

### Breaking It Down

We'll start by doing some design on our code - we'll identify the 'stuff' we need to get done for our game to look like
the example output.

There are some high level chunks we can break it up into:

1. Welcome the player to the game
2. Ask for a number
3. Check if the number is correct. If it is, end the game, the player won!
4. Calculate the number of hints the player gets from the guess
5. Show the hints
6. Repeat step 2 unless there are no more turns left
7. Show the game over screen

We'll try and go through these step by step!

### Welcome the Player

This is nice and simple - we just send a little welcome message to the player when they join. I like to also tell them
the goal of the game here too!

```python
print("Welcome to Mastermind! You have to determine a number between 100-999, using hints from your previous guesses!")
```

Before we can ask for a number, we need a number for them to guess! This is where the `random` library we brought in
earlier is useful. We can generate a random integer, and then convert it to a string. We'll see why its better to be a
string later.

```python
secret = str(random.randint(100, 999))
```

We now have a secret number! But we're still missing something. If we jump straight into letting them guess, they'll
make their guess, get it right or wrong, and then the game will end. That's not how it's supposed to work! We need to
add the number of turns the player can take! We do this by adding *another* while loop, and having a counter for how
many turns the player has left.

```python
turns_left = 8  # I chose 8 because it's a good challenge! Feel free to pick your own number!

while turns_left > 0:

# Most of our stuff will go in here now!

```

### Guess Master

We need to prompt our player for a guess. We've done something similar in our core game loop - it asks for a prompt!
Let's do that again, but ask for a number.

```python
guess = input("Guess a number: ")
```

But wait - we can't just accept any random input! It has to be a number between 100 and 999. There are a lot of ways to
check this, but the easiest way for us is to check the length of the number they put in. If they put in a number that's
too short or too long, we can detect it. This approach won't catch if the player tries to type in something that isn't a
number, but that's okay, we're not trying to over-complicate it.

The process of checking our player types in is what's known as validating user input. It's a very common thing to do in
programming, so you'll have to get used to your users typing in the wrong thing!

```python
if len(guess) != 3:
    print("Must be a number 100-999")
```

We'll also need to make sure that they get re-prompted for input if they get it wrong. Since we don't know when they'll
get it right, we use a while loop to run until they get it right. Here's what we'll need to make that work.

```python
guess = input("Guess a number:")
while len(guess) != 3:
    print("Must be a number 100-999")
    guess = input("Guess a number: ")
```

### Checking if they got it right

Now we have their guess, we need to check if they got it right. This is fortunately a really easy thing to do! If the
players guess is correct, then it will be an exact match with the secret number, and we can skip the turn counter early.

```python
if guess == secret:
    print("You got it!")
    break  # This gets us out of the turn loop, but still inside the core gameplay loop. Nice!
```

### Calculating the hints

This section is easily the most complicated section. This part is the heart of the game, as it does all the hard work
calculating the result of the guess.

Before we dive into the code, we need to understand how the hints work. In the Mastermind game, there are 2 types of
hints - correct position hints and correct number hints. The correct position hints are based on both a match of number
and position for the guess. The correct number hints are based only on if the number is correct, the position doesn't
matter. A really important bit to note is that the correct position hints are calculated BEFORE the correct number
hints. If you get the position hint, then it's already assumed you got the number hint as well, so there is no number
hint awarded for position hints. An example:

```
Guess: 122
Secret: 123
```

In this case, the player should get 2 position hints, and 0 correct number hints. The player got the 1 and 2 correct.
That only leaves the last numbers left - and 2 is not 3, so they don't get the correct number hint.

A good way to think about it is that the position hints 'cross off' the correct positions when checking the correct
number hints. The example before could be shown in 2 steps:

```
Guess: 122
Secret: 123
```

Applying the position hint check:

```
Guess: **2
Secret: **3
```

2 position hints. Applying the correct number check:

```
Guess: **2
Secret: **3
```

0 number hints.

Wow. That was a lot to take in! Don't worry if you couldn't keep up with the logic - this stuff is complicated! Solving
problems like these is what software engineers do on a daily basis - it's a game of forever solving riddles and complex
logic puzzles while writing it in a way that a computer can understand!

If you think you're up to the task, I commend you if take on the challenge to try and implement the checks. But no
biggie if you can't figure it out - I've provided the code with comments that explain everything.

```python
number_correct = 0  # number but not position correct
position_correct = 0  # number and position correct

# create a list of all numbers that aren't position correct
guess_list = []
secret_list = []

# the 'zip' function is just a neat way to iterate over 2 lists at the same time
for g, s in zip(guess, secret):  # This is why we need the secret to be a string - so we can use a loop on it!
    if g == s:
        position_correct += 1  # Exact match, so it must be position correct
    else:
        guess_list.append(g)  # Not an exact match, so we need to check these numbers again
        secret_list.append(s)

for g in guess_list:
    if g in secret_list:  # If the guess is in the not-exact match, it must be a correct number.
        number_correct += 1
        secret_list.remove(g)
```

That was a lot of code! Take it step by step, and make sure you get the spacing right - there's a lot going on!

If you managed to get it in, you've made a huge effort - that was a tough algorithm to crack.

### Show the hints

Now that we've calculated the hints, it's time to let the player know how they went! Make sure this is in the turn loop,
so it should be in line with the for loops from the hint calculation.

```python
print("That guess got", position_correct, "numbers in the right position and", number_correct, "other correct numbers.")
```

### Counting our turns

We tackled most of the turn-based stuff in the welcome section by adding the while loop that uses the `turns_left`
counter. Since we've reached the end of the turn, we need to decrement the counter by one.

```python
turns_left -= 1
```

### Show the Game Over screen

Our player has reached the end of the road - they've run out of turns! When we leave the `turns_left` loop, there are 2
reasons we've left:

1. The player won the game by guessing correctly
2. The player lost the game by running out of guesses

To make sure we don't show the game over screen to players that won, we need to check if they ran out of turns, then we
can show the game over screen. Make sure this is *outside* the `turns_left` loop, but still inside the core game loop.

Our game over screen should contain 2 things. The first is a message letting the player know they've lost. The second is
the secret number! It would really suck to be 1 guess of getting it correct and then never knowing if you actually got
it correct. By adding the secret number, we make sure our players get to know how close they were.

```python
if turns_left == 0:
    print("Good try! The secret number was", secret)
```
    
### The Finished Game

Great job for making it to the end! we've now finished our game - if you run it in your Python environment, we now have
a playable Mastermind game we can play at any time!

If you got stuck at any point or want to compare your solution with the full code, you can access it [here](./main.py)

# Further Challenges

If you want to challenge yourself further after completing this activity, there are a bunch of improvements you can
make!

* Add pauses by using the `time` library and `time.sleep()` so players have more time to read the text
* Add more information to the welcome message to help new players learn how to play
* Let the player know how many turns they have left each time they guess
* Change the number of guesses or length of the secret number to make it harder