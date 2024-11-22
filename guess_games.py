import random

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
    # Number of your attemps in word guess
    attempts = 6
    
    print("Welcome to 'Guess the Word' game!")
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
            print(f"Congratulations! You've guessed the word: {word} you are ginius")
            print("----------------------------------")
            break
    else:
        # Print if the attemps of user became 0
        print(f"Game Over! The word was: {word}")

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
            # If users input is invalid
            print("Invalid choice. Please choose  ([1], [2], [3]). ")

    # Numbers of attemps in Guess number
    attempts = 10
    print(f"Welcome to 'Guess the Number' game!")
    print("----------------------------------")
    
        
       
# Function for the Guess the Map game
def guess_the_map():
    pass

# Main choice to select the game you want to play
def main_choice():
    print("----------------------------------")
    print("Welcome to the Guessing Game!")
    print("----------------------------------")
    print("Choose type of Game:\n")
    print("[1] Guess the Word")
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
