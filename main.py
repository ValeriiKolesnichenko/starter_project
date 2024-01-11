"""There is an entertaing chat-bot, it will make your day funny)"""
from time import sleep
from colorama import Fore, Style
import funcs

# Greeting
print(f"{Fore.BLUE} Hello! I'm glad to see you!{Style.RESET_ALL}")
while True:
    # Menu
    bot_menu: str = f"""{Fore.YELLOW} Here are the list of choices {Style.RESET_ALL} {Fore.BLUE}
    1. Tell me a joke
    2. Game 'Guess the number'
    3. Recommend a movie
    4. Recommend a computer game.
    5. Exit.{Style.RESET_ALL}"""
    print(bot_menu)

    # Choice variable
    choice: str = input(f"{Fore.GREEN} What's the option do you want to select? {Style.RESET_ALL}")

    # Handling all the possible choices
    if choice == '1':
        print("...")
        sleep(3)
        funcs.take_joke()
    elif choice == '2':
        print("...")
        sleep(3)
        funcs.guess_the_number()
    elif choice == '3':
        print("...")
        sleep(3)
        print("There are the best movies in my opinion!")
        funcs.recommend_movie()
    elif choice == '4':
        print("...")
        sleep(3)
        print("There are the best games in my opinion!")
        funcs.recommend_game()
    elif choice == '5':
        sleep(1)
        print("Thanks for having a great time!")
        sleep(2)
        print('Closing...')
        sleep(2)
        break
    else:
        print('...')
        sleep(3)
        print("This choice does not exist. Try again!")
