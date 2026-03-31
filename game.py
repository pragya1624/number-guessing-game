import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("\nGuess the number between 1 and 100!")

    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break

while True:
    play_game()
    again = input("\nPlay again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Goodbye!")
        break

