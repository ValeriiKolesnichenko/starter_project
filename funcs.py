"""The functions, which determines the main logic of the project"""
from random import randint
import pyjokes
from colorama import Fore, Style
from prettytable import PrettyTable

def take_joke() -> None:
    """The function, which returns the random joke, using pyjokes module"""
    joke = pyjokes.get_joke()
    print(joke)

def guess_the_number() -> None:
    """The lodic of the game 'Guess the number'."""
    # Generating a random number
    random_number: int = randint(1, 100)
    # The start quantity of attempts
    attempts: int = 0
    while True:
        # 20-26 lines handle special inputs from user.
        number: str = input(f"""{Fore.YELLOW}Try to guess the number! (q - quit) {Style.RESET_ALL}""")
        if number.lower() == 'q':
            print(f"Game over. The quessed number was {random_number}")
            break
        if not number.isdigit():
            print("You entered an incorrect value. Please, enter the integer.")
            continue

        # If user enters a correct value, he'll come to this piece of code
        user_number = int(number)
        attempts += 1
        if user_number > random_number:
            print("Number, that I've proposed a bit less. Try again!")
        elif user_number < random_number:
            print("Number, that I've proposed a bit more. Try again!")
        elif user_number == random_number:
            print(f"{Fore.LIGHTBLUE_EX}That's it! You are great! "
                  f"You quessed the number {random_number} for {attempts} attempts. "
                  f"Do you want to play one more time?{Style.RESET_ALL}")

def recommend_movie() -> None:
    """Movies recommendation, using prettytable-module for generating beautiful table."""
    table: PrettyTable = PrettyTable()
    table.field_names = ['ID', 'Title', 'Genre', 'Rating', 'Year', 'Directed by']
    table.add_rows([
        [1, 'Interstellar', 'Science fiction', '92 %', 2014, 'Christopher Nolan'],
        [2, 'Shutter Island', 'Mystery & thriller, Drama', '89 %', 2010, ' Martin Scorsese'],
        [3, 'Inception', 'Science fiction', '88 %', 2010, 'Christopher Nolan'],
        [4, 'The Butterfly Effect', 'Science fiction thriller', '86 %', 2004, 'Anthony Rhulen'],
        [5, 'Troy', 'Historical', '86 %', 2004, 'Wolfgang Petersen'],
        [6, 'Law Abiding Citizen', 'Drama thriller', '85 %', 2009, 'F. Gary Gray'],
        [7, 'American Pie', 'Comedy', '85 %', 1999, 'Paul Weitz'],
        [8, 'Limitless', 'Science fiction, thriller', '84 %', 2011, 'Neil Burger'],
        [9, 'The Prestige', 'Thriller', '81 %', 2006, 'Christopher Nolan'],
        [10, 'Drag Me to Hell', 'Horror', '81 %', 2009, 'Sam Raimi'],
    ])
    print(table)

def recommend_game() -> None:
    """Games recommendation, using prettytable-module for generating beautiful table."""
    table: PrettyTable = PrettyTable()
    table.field_names = ['ID', 'Title', 'Genre', 'Rating', 'Year', 'Developed by']
    table.add_rows([
        [1, 'Resident Evil 7: Biohazard', 'Survival horror', '93 %', 2017, 'Capcom'],
        [2, 'Dying Light', 'Survival horror', '87 %', 2015, 'Techland'],
        [3, 'Far Cry 3', 'First-person shooter', '90 %', 2012, 'Ubisoft Montreal'],
        [4, 'The Sinking City', 'Action-adventure, detective', '88 %', 2019, 'Frogwares'],
        [5, 'Dark Souls 3', 'RPG', '89 %', 2016, 'FromSoftware'],
        [6, 'Dead Island', 'RPG', '84 %', 2011, 'Techland'],
        [7, 'Grand Theft Auto V', 'Action-adventure', '92 %', 2013, 'Rockstar North'],
        [8, 'The Witcher 3: Wild Hunt', 'RPG', '86 %', 2015, 'CD Projekt Red'],
        [9, 'Red Dead Redemption 2', ' Action-adventure', '92 %', 2018, 'Rockstar Games'],
        [10, 'DOOM', 'Shooter', '85 %', 2016, 'id Software'],
    ])
    print(table)

# recommend_movie()
# recommend_game()
# guess_the_number()
