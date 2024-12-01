import random
import emoji

# List of words to guess from and their clues
word_list = [
    ("pyhton", "It's a Snake."),
    ("java", "It's a Coffee."),
    ("ruby", "It's a Red Diamond."),
    ("html", "Web Development"),
    ("machine", "1 or 0 coding."),
    ("basket", "It's a container used for storing clean or dirty clothes."),
]

# Function to select a random word and its clue
def choose_word():
    return random.choice(word_list)

# Function to display the word with blanks for unguessed letters
def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Function for the Guess the Word game
def guess_the_word():
    # Choose a random word and its clue
    word, clue = choose_word()
    # Store your guessed letters
    guessed_letters = []
    # Number of your attempts
    attempts = 6

    print("Welcome to 'Guess Program Language' game!")
    print("----------------------------------")
    print(f"You got {attempts} attempts!")
    print(f"Clue: {clue}")

    while attempts > 0:
        print("\nWord to guess: " + display_word(word, guessed_letters))
        print(f"You have {attempts} attempts left.")

        # Ask for user input
        print("----------------------------------")
        guess = input("Enter a letter: ").lower()
        print("----------------------------------")

        # Check if input of user is only a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Print if the user enter the letter that already guessed
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try a different one.")
            continue

        guessed_letters.append(guess)

        # Function that check if the user guess the rigth letter in the word
        if guess in word:
            print(f"Your are Smart! The letter '{guess}' is in the word.")
            print("----------------------------------")
        else:
            attempts -= 1
            print(f"Oops! Sorry the letter '{guess}' is not in the word guess.")
            print("----------------------------------")

        # Function that check if player has guessed all letters
        if all(letter in guessed_letters for letter in word):
            print(emoji.emojize(f"Congratulations! You've guessed the word: {word}. You are a genius :thumbs_up:"))
            print("----------------------------------")
            break
    else:
        # Print if the attempts of user became 0
        print (emoji.emojize(f"Game Over! The word was: {word}! :thumbs_down:"))

# Function for the Guess the Number game
def guess_the_number():
    # Level selection
    print("Choose a level:\n")
    print("[1] Easy (1 - 15)")
    print("[2] Medium (20 - 40)")
    print("[3] Hard (60 - 100)")

    while True:
        print("----------------------------------")
        level = input("Enter Level ([1], [2], [3]): ")
        print("__________________________________")
        print("----------------------------------")
        # level 1 1 - 15
        if level == '1':
            number_to_guess = random.randint(1, 15)
            break
        # level 2 20 - 40
        elif level == '2':
            number_to_guess = random.randint(20, 40)
            break
        # level 3 60 - 100
        elif level == '3':
            number_to_guess = random.randint(60, 100)
            break
        else:
            print("Invalid choice. Please choose ([1], [2], [3]). ")

    attempts = 10
    print(f"Welcome to 'Guess the Number' game!")
    print("----------------------------------")
    print(f"You have {attempts} attempts!")
    print(f"Try to guess a number between the given range based on the level.")

    while attempts > 0:
        print("----------------------------------")
        guess = input(f"Enter your guess (between {1 if level == '1' else 20 if level == '2' else 60} and {15 if level == '1' else 40 if level == '2' else 100}): ")

        # Check if the input is a valid number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        # Check if guess is within the range of the level
        if level == '1' and not 1 <= guess <= 15:
            print(f"Please guess a number between 1 and 15.")
            continue
        elif level == '2' and not 20 <= guess <= 40:
            print(f"Please guess a number between 20 and 40.")
            continue
        elif level == '3' and not 60 <= guess <= 100:
            print(f"Please guess a number between 60 and 100.")
            continue

        # Check if the guess is correct
        if guess == number_to_guess:
            print(emoji.emojize(f"Congratulations! You've guessed the number {number_to_guess}!:thumbs_up:"))
            break
        else:
            attempts -= 1
            if guess < number_to_guess:
                print("Your guess is too low!")
            else:
                print("Your guess is too high!")
            print(f"You have {attempts} attempts left.")
    else:
        print(emoji.emojize(f"Game Over! The number was: {number_to_guess}! :thumbs_down:"))

# Function for the Guess the Map game
def guess_the_map():
    # List of cities and their clues
    cities = [
        ("paris", "The city of love, known for the Eiffel Tower."),
        ("london", "Capital city of the UK, famous for the Big Ben."),
        ("tokyo", "Capital of Japan, known for its technology and cherry blossoms."),
        ("newyork", "City that never sleeps, home of the Statue of Liberty."),
        ("sydney", "Known for the Opera House and Harbour Bridge in Australia."),
    ]

    # Randomly select a city and its clue
    city, clue = random.choice(cities)

    # Store your guessed letters and attempts
    guessed_letters = []
    attempts = 5  # Set a lower number of attempts for a guessing game like this

    print("Welcome to 'Guess the Map' game!")
    print("----------------------------------")
    print(f"You have {attempts} attempts!")
    print(f"Clue: {clue}")

    while attempts > 0:
        # Display the city name with blanks for unguessed letters
        display_city = ''.join([letter if letter in guessed_letters else '_' for letter in city])
        print(f"\nCity to guess: {display_city}")
        print(f"You have {attempts} attempts left.")

        # Ask for user input
        print("----------------------------------")
        guess = input("Enter a letter: ").lower()
        print("----------------------------------")

        # Check if input is only a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try a different one.")
            continue

        # Add guessed letter to the list
        guessed_letters.append(guess)

        # Check if the guessed letter is in the city name
        if guess in city:
            print(f"Great job! The letter '{guess}' is in the city.")
        else:
            attempts -= 1
            print(f"Oops! The letter '{guess}' is not in the city.")

        # Check if the player has guessed all letters in the city name
        if all(letter in guessed_letters for letter in city):
            print (emoji.emojize(f"Congratulations! You've guessed the city: {city}. Well done!:thumbs_up:"))
            break
    else:
        print (emoji.emojize(f"Game Over! The city was: {city}! :thumbs_down:"))

# Main choice to select the game you want to play
def main_choice():
    print("----------------------------------")
    print("Welcome to the Guessing Game!")
    print("----------------------------------")
    print("Choose type of Game:\n")
    print("[1] Guess the Programming Language")
    print("[2] Guess the Number")
    print("[3] Guess the City")
    print("\n----------------------------------")

    while True:
        choice = input("Enter Choice ([1], [2], [3]): ")
        print("__________________________________")
        print("----------------------------------")

        if choice == "1":
            guess_the_word()
            break
        elif choice == "2":
            guess_the_number()
            break
        elif choice == "3":
            guess_the_map()
            break
        else:
            print("Invalid choice. Please choose ([1], [2], [3]).")

if __name__ == "__main__":
    main_choice()
