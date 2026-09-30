target = 27
limit = 5

tries = 0
player_guess = 0

print("=" * 42)
print("NUMBER GUESSING GAME")
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print()

while tries < limit and player_guess != target:
    player_guess = int(input("Enter your guess: "))
    tries += 1

    if player_guess == target:
        print(f"Correct! You guessed it in {tries} attempt(s)!")
    else:
        if player_guess > target:
            gap = player_guess - target
        else:
            gap = target - player_guess

        if gap >= 20:
            print("Ice cold!")
        elif gap >= 10:
            print("Cold!")
        elif gap >= 5:
            print(" Warm!")
        else:
            print("Hot!")

        lives_left = limit - tries
        if lives_left > 0:
            for i in range(lives_left):
                print("", end="")
            print()

if player_guess != target:
    print(f"Game over! The secret number was {target}.")