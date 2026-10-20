import random 
lowest_number = 1
highest_number = 100 
number = random.randint(lowest_number, highest_number+1)
guesses = 0
print(f"Welcome to the Guess the Number Game! I have selected a number between {lowest_number} and {highest_number}. Can you guess what it is?")
running = True

while running:
    guess = (input(f"Guess a number between {lowest_number} and {highest_number} :"))
    guesses += 1

    if guess.isdigit() :
        guess = int(guess)
        if guess == number:
            print(f"Congratulations! You have guessed the right number which is {number}. It took you {guesses} guesses.")
            running = False
        elif guess < number:
            print("Your guess is too low. Try again.")
        elif guess > number:
            print("Your guess is too high. Try again.")

    else:
        print("Please enter a valid number.")
        print("Try again.")

   
    

