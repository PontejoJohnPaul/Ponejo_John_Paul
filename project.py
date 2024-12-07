import random
import emoji
import csv
import os

def load_word_list():
    word_list = {}
    file_path = "C:\\Users\\ponte\\OneDrive\\Desktop\\ProjectACP\\project\\word_list.csv"
    
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        exit()
    
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        # Skip header
        next(csv_reader) 
        for row in csv_reader:
            if len(row) == 2:
                 # Map clue to word
                word_list[row[1]] = row[0]
    # Return the dictionary
    return word_list 

# Function to initialize the game results CSV
def init_game_results_csv():
    file_path = "C:\\Users\\ponte\\OneDrive\\Desktop\\ProjectACP\\project\\game_results.csv"
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            # Write the header if the file doesn't exist
            csv_writer.writerow(["Name", "Game", "Attempts", "Word/City/Number"])

# Function to write results to the CSV file, updating if the name already exists
def write_game_results(name, game, attempts, word_or_city):
    file_path = "C:\\Users\\ponte\\OneDrive\\Desktop\\ProjectACP\\project\\game_results.csv"
    
    # Read existing data from CSV
    rows = []
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
    
    # Check if the player already exists
    player_exists = False
    for row in rows:
        if row[0] == name and row[1] == game:
            # Add attempts to the existing total
            row[2] = str(int(row[2]) + attempts)  
            # Update the word or city
            row[3] = word_or_city 
            player_exists = True
            break

    # If player doesn't exist, append a new row
    if not player_exists:
        rows.append([name, game, str(attempts), word_or_city])
    
    # Write the updated data back to CSV
    with open(file_path, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(rows)

# Load word list from CSV
def load_word_list():
    word_list = []
    file_path = "C:\\Users\\ponte\\OneDrive\\Desktop\\ProjectACP\\project\\word_list.csv"
    
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        exit()
    
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if len(row) == 2:
                word_list.append((row[0].lower(), row[1]))
    return word_list

# Load city list from CSV
def load_city_list():
    city_list = []
    file_path = "C:\\Users\\ponte\\OneDrive\\Desktop\\ProjectACP\\project\\cities_list.csv"
    
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        exit()

    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        try:
            header = next(csv_reader)
            if len(header) != 2:
                print(f"Error: The header in '{file_path}' is not valid. Expected 2 columns.")
                exit()
        except StopIteration:
            print(f"Error: The CSV file '{file_path}' is empty.")
            exit()

        for row in csv_reader:
            if len(row) == 2:
                # Add city and clue to the list
                city_list.append((row[0].lower(), row[1]))  
            else:
                print(f"Warning: Row '{row}' in '{file_path}' is not valid. Expected 2 columns.")

    if not city_list:
        print(f"Error: No valid city data found in '{file_path}'.")
        exit()

    return city_list

# Function to choose a random word and its clue from the word list
def choose_word():
    word_list = load_word_list() 
    return random.choice(word_list) 

# Function to choose a random city and its clue from the city list
def choose_city():
    city_list = load_city_list()
    # Randomly choose a city
    return random.choice(city_list)  

# Function to display the word with blanks for unguessed letters
def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Method for the Guess the Word game
def guess_the_word(name):
    word, clue = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to 'Guess the Programming Language' game!")
    print("----------------------------------")
    print(f"You got {attempts} attempts!")
    print(f"Clue: {clue}")
    print("----------------------------------")

    while attempts > 0:
        print("\nWord to guess: " + display_word(word, guessed_letters))
        print(f"You have {attempts} attempts left.")
        print("----------------------------------")
        guess = input("Enter a letter: ").lower()
        print("----------------------------------")

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try a different one.")
            continue
        
        guessed_letters.append(guess)

        if guess in word:
            print(f"You're smart! The letter '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Oops! Sorry, the letter '{guess}' is not in the word.")

        if all(letter in guessed_letters for letter in word):
            print(emoji.emojize(f"Congratulations! You've guessed the word: {word}. :thumbs_up:"))
            break
    else:
        print(f"Game Over! The word was: {word}!")

    write_game_results(name, "Guess the Programming Language", attempts, word)

# Function for the Guess the Number game
def guess_the_number(name):
    print("Choose a level:\n")
    print("[1] Easy (1 - 15)")
    print("[2] Medium (20 - 40)")
    print("[3] Hard (60 - 100)")
    print("----------------------------------")

    while True:
        level = input("Enter Level ([1], [2], [3]): ")
        print("__________________________________")

        if level == '1':
            number_to_guess = random.randint(1, 15)
            break
        elif level == '2':
            number_to_guess = random.randint(20, 40)
            break
        elif level == '3':
            number_to_guess = random.randint(60, 100)
            break
        else:
            print("Invalid choice. Please choose ([1], [2], [3]). ")
            continue

    attempts = 10
    print(f"You have {attempts} attempts!")
    print(f"Try to guess a number between the given range based on the level.")
    print("----------------------------------")

    while attempts > 0:
        guess = input(f"Enter your guess (between {1 if level == '1' else 20 if level == '2' else 60} and {15 if level == '1' else 40 if level == '2' else 100}): ")
        print("----------------------------------")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if level == '1' and not 1 <= guess <= 15:
            print(f"Please guess a number between 1 and 15.")
            continue
        elif level == '2' and not 20 <= guess <= 40:
            print(f"Please guess a number between 20 and 40.")
            continue
        elif level == '3' and not 60 <= guess <= 100:
            print(f"Please guess a number between 60 and 100.")
            continue

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
        print(f"Game Over! The number was: {number_to_guess}!")

    write_game_results(name, "Guess the Number", attempts, number_to_guess)

# Function for the Guess the Map game
def guess_the_map(name):
    city, clue = choose_city()  # Get a random city and its clue
    guessed_letters = []
    attempts = 5

    print("Welcome to 'Guess the Map' game!")
    print("----------------------------------")
    print(f"You have {attempts} attempts!")
    print(f"Clue: {clue}")  # Display the clue at the start
    print("----------------------------------")

    while attempts > 0:
        display_city = ''.join([letter if letter in guessed_letters else '_' for letter in city])
        print(f"\nCity to guess: {display_city}")
        print(f"You have {attempts} attempts left.")
        print("----------------------------------")
        guess = input("Enter a letter: ").lower()
        print("----------------------------------")

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try a different one.")
            continue

        guessed_letters.append(guess)

        if guess in city:
            print(f"Great job! The letter '{guess}' is in the city.")
        else:
            attempts -= 1
            print(f"Oops! The letter '{guess}' is not in the city.")

        if all(letter in guessed_letters for letter in city):
            print(emoji.emojize(f"Congratulations! You've guessed the city: {city}. :thumbs_up:"))
            break
    else:
        print(f"Game Over! The city was: {city}!")
    write_game_results(name, "Guess the City", attempts, city)

# Main choice to select the game you want to play
def main_choice():
    # Initialize CSV if it doesn't exist
    init_game_results_csv() 

    # Ask for the user's name
    print("----------------------------------")
    name = input("Please enter your name: ")  
    print("----------------------------------")
    while True:
        print("Welcome to the Guessing Game!")
        print("----------------------------------")
        print("Choose type of Game:\n")
        print("[1] Guess the Programming Language")
        print("[2] Guess the Number")
        print("[3] Guess the City")
        print("----------------------------------")

        while True:
            choice = input("Enter Choice ([1], [2], [3]): ")
            print("__________________________________")

            if choice == "1":
                guess_the_word(name)
                break
            elif choice == "2":
                guess_the_number(name)
                break
            elif choice == "3":
                guess_the_map(name)
                break
            else:
                print("Invalid choice. Please choose ([1], [2], [3]).")
                continue

        play_again = input("Do you want to play again? (y/anything): ").lower()
        print("__________________________________")
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main_choice()
