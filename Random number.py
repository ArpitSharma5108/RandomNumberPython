import random
print("Welcome to number guessing game\nYou have 7 chances to guess the number....")

low = int(input("Enter lower number"))
high = int(input("Enter higher number"))

print(f"You can choose numbers between {low} to {high}")

num = random.randint(low, high)
chances = 7
guesses = 0

while guesses<chances:
    guesses+=1
    guess = int(input("Enter your guess..."))

    if guess == num:
        print(f"Congtatulation the number is {num} and you have guessed in {guesses} attempts")
        break
    elif guesses>chances and guess!=num:
        print("You have no more guesses left, better luck next time...")
    elif guess>num:
        print("Your guess is high...")
    elif guess<num:
        print("Your guess is low...")