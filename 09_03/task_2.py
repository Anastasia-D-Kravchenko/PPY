import random

target = random.randint(1, 100)
guesses = []

print("Guess the number between 1 and 100!")

while True:
    guess = int(input("Guess a number: "))
    guesses.append(guess)

    if guess < target:
        print("Too small!")
    elif guess > target:
        print("Too large!")
    else:
        print("Correct!")
        break
print(f"Attempts: {len(guesses)}")
print(f"Last 3 guesses: {guesses[-3:]}")