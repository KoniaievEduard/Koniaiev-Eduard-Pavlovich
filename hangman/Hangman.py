import random

start_stop = True
while start_stop:

    # Главное меню

    menu_of_game = input("   WELCOME TO THE HANGMAN!!!\nDo you want to start the game ?(yes/no)\nUser: ")
    if menu_of_game == "Yes" or menu_of_game == "yes":

    # Начало игры

        print("Okey! You have to guess the word. Lets do this!")

    # Выбор слова

        word_list = ["python", "java", "javascript", "php"]
        word = (random.choice(word_list))

    # Анализ прогресса

        if word == "python":
            defiz1 = "-"
            defiz2 = "-"
            defiz3 = "-"
            defiz4 = "-"
            defiz5 = "-"
            defiz6 = "-"
            tries = 8
            print("You have", tries, "tries")
            print("please, input a letter.")
            while True:
                print(defiz1, defiz2, defiz3, defiz4, defiz5, defiz6)
                if defiz1 == "p" and defiz2 == "y" and defiz3 == "t" \
                        and defiz4 == "h" and defiz5 == "o" and defiz6 == "n":
                    print("You survive!")
                    main_menu = input("Pleas, press 'Enter' to exit in main menu")
                    break
                letter = input("User:")
                if len(letter) > 1:
                    print("You should input a single letter.")
                if letter.isupper():
                    print("Please enter a lowercase English letter.")
                if defiz1 == "p" and letter == "p":
                    print("You've already guessed this letter.")
                elif defiz2 == "y" and letter == "y":
                    print("You've already guessed this letter.")
                elif defiz3 == "t" and letter == "t":
                    print("You've already guessed this letter.")
                elif defiz4 == "h" and letter == "h":
                    print("You've already guessed this letter.")
                elif defiz5 == "o" and letter == "o":
                    print("You've already guessed this letter.")
                elif defiz6 == "n" and letter == "n":
                    tries -= 1
                    print("No improvements")
                if letter == "p":
                    defiz1 = "p"
                elif letter == "y":
                    defiz2 = "y"
                elif letter == "t":
                    defiz3 = "t"
                elif letter == "h":
                    defiz4 = "h"
                elif letter == "o":
                    defiz5 = "o"
                elif letter == "n":
                    defiz6 = "n"
                else:
                    print("That letter doesn't appear in the word")
                    tries -= 1
                print("You have", tries, "tries")
                if tries <= 0:
                    print("You lost!")
                    main_menu = input("Pleas, press 'Enter' to exit in main menu")
                    break
        elif word == "java":
            defiz1 = "-"
            defiz2 = "-"
            defiz3 = "-"
            defiz4 = "-"
            tries = 8
            print("You have", tries, "tries")
            print("please, input a letter.")
            while True:
                print(defiz1, defiz2, defiz3, defiz4)
                if defiz1 == "j" and defiz2 == "a" and defiz3 == "v" and defiz4 == "a":
                    print("You survive!")
                    main_menu = input("Pleas, press 'Enter' to exit in main menu")
                    break
                letter = input("User:")
                if len(letter) > 1:
                    print("You should input a single letter.")
                if letter.isupper():
                    print("Please enter a lowercase English letter.")
                if defiz1 == "j" and letter == "j":
                    print("You've already guessed this letter.")
                elif defiz2 == "a" and letter == "a":
                    print("You've already guessed this letter.")
                elif defiz3 == "v" and letter == "v":
                    print("You've already guessed this letter.")
                elif defiz4 == "a" and letter == "a":
                    print("You've already guessed this letter.")
                if letter == "j":
                    defiz1 = "j"
                elif letter == "a":
                    defiz2 = "a"
                    defiz4 = "a"
                elif letter == "v":
                    defiz3 = "v"
                else:
                    print("That letter doesn't appear in the word")
                    tries -= 1
                print("You have", tries, "tries")
                if tries <= 0:
                    print("You lost!")
                    main_menu = input("Pleas, press 'Enter' to exit in main menu")
                    break
        elif word == "javascript":
            defiz1 = "-"
            defiz2 = "-"
            defiz3 = "-"
            defiz4 = "-"
            defiz5 = "-"
            defiz6 = "-"
            defiz7 = "-"
            defiz8 = "-"
            defiz9 = "-"
            defiz10 = "-"
            tries = 10
            print("You have", tries, "tries")
            print("please, input a letter.")
            while True:
                print(defiz1, defiz2, defiz3, defiz4, defiz5, defiz6, defiz7, defiz8, defiz9, defiz10)
                if defiz1 == "j" and defiz2 == "a" and defiz3 == "v" \
                    and defiz4 == "a" and defiz5 == "s" and defiz6 == "c" \
                    and defiz7 == "r" and defiz8 == "i" and defiz9 == "p" \
                    and defiz10 == "t":
                    print("You survive!")
                    main_menu = input("Pleas, press 'Enter' to exit in main menu")
                    break
                letter = input("User:")
                if len(letter) > 1:
                    print("You should input a single letter.")
                if letter.isupper():
                    print("Please enter a lowercase English letter.")
                if defiz1 == "j" and letter == "j":
                    print("You've already guessed this letter.")
                elif defiz2 == "a" and letter == "a":
                    print("You've already guessed this letter.")
                elif defiz3 == "v" and letter == "v":
                    print("You've already guessed this letter.")
                elif defiz4 == "a" and letter == "a":
                    print("You've already guessed this letter.")
                elif defiz5 == "s" and letter == "s":
                    print("You've already guessed this letter.")
                elif defiz6 == "c" and letter == "c":
                    print("You've already guessed this letter.")
                elif defiz7 == "r" and letter == "r":
                    print("You've already guessed this letter.")
                elif defiz8 == "i" and letter == "i":
                    print("You've already guessed this letter.")
                elif defiz9 == "p" and letter == "p":
                    print("You've already guessed this letter.")
                elif defiz10 == "t" and letter == "t":
                    print("You've already guessed this letter.")
                if letter == "j":
                    defiz1 = "j"
                elif letter == "a":
                    defiz2 = "a"
                    defiz4 = "a"
                elif letter == "v":
                    defiz3 = "v"
                elif letter == "s":
                    defiz5 = "s"
                elif letter == "c":
                    defiz6 = "c"
                elif letter == "r":
                    defiz7 = "r"
                elif letter == "i":
                    defiz8 = "i"
                elif letter == "p":
                    defiz9 = "p"
                elif letter == "t":
                    defiz10 = "t"
                else:
                    print("That letter doesn't appear in the word")
                    tries -= 1
                print("You have", tries, "tries")
                if tries <= 0:
                    print("You lost!")
                    main_menu = input("Pleas, press 'Enter' to exit in main menu")
                    break
        elif word == "php":
            defiz1 = "-"
            defiz2 = "-"
            defiz3 = "-"
            tries = 8
            print("You have", tries, "tries")
            print("please, input a letter.")
            while True:
                print(defiz1, defiz2, defiz3)
                if defiz1 == "p" and defiz2 == "h" and defiz3 == "p":
                    print("You survive!")
                    main_menu = input("Pleas, press 'Enter' to exit in main menu")
                    break
                letter = input("User:")
                if len(letter) > 1:
                    print("You should input a single letter.")
                if letter.isupper():
                    print("Please enter a lowercase English letter.")
                if defiz1 == "p" and letter == "p":
                    print("You've already guessed this letter.")
                elif defiz2 == "h" and letter == "h":
                    print("You've already guessed this letter.")
                elif defiz3 == "p" and letter == "p":
                    print("You've already guessed this letter.")
                if letter == "p":
                    defiz1 = "p"
                    defiz3 = "p"
                elif letter == "h":
                    defiz2 = "h"
                else:
                    print("That letter doesn't appear in the word")
                    tries -= 1
                    print("You have", tries, "tries")
                if tries <= 0:
                    print("You lost!")
                    main_menu = input("Pleas, press 'Enter' to exit in main menu")
                    break
        else:
            print("You lost")
            main_menu = input("Pleas, press 'Enter' to exit in main menu")
    else:
        start_stop = False