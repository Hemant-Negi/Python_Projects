import random

def hangman():
    word = random.choice(
        ["ayush", "malan", "saxena", "hemant", "neeru", "rajni", "cheenu", "spiron"])
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ""
    while(len(word) > 0):
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main+letter
            else:
                main = main+"_"+""
        if main == word:
            print(main, "\nYOU WON!!!"+name)
            break
        print("Guess the word:>", main)
        guess = input()

        if guess in validletters:
            guessmade = guessmade+guess
        else:
            print("enter a valid character:")
            guess = input("enter again")
        if guess not in word:
            turns -= 1
            if turns == 9:
                print("9 turns left: ")
                print("-------")
            if turns == 8:
                print("8 turns left: ")
                print("-------")
                print("   O   ")
            if turns == 7:
                print("7 turns left: ")
                print("-------")
                print("   O   ")
                print("   |   ")
            if turns == 6:
                print("6 turns left: ")
                print("-------")
                print("   O   ")
                print("   |   ")
                print("  /    ")
            if turns == 5:
                print("5 turns left: ")
                print("-------")
                print("   O   ")
                print("   |   ")
                print("  / \  ")
            if turns == 4:
                print("5 turns left: ")
                print("-------")
                print("  \O   ")
                print("   |   ")
                print("  / \  ")
            if turns == 3:
                print("3 turns left: ")
                print("-------")
                print("  \O/  ")
                print("   |   ")
                print("  / \  ")
            if turns == 2:
                print("2 turns left: ")
                print("-------")
                print("  \O/__")
                print("   |   ")
                print("  / \  ")
            if turns == 1:
                print("1 turns left: ")
                print("Last Chance!!!!")
                print("-------")
                print("  \O/_| ")
                print("   |    ")
                print("  / \   ")
            if turns == 0:
                print("YOUR MAN DIED>>>")
                print("-------")
                print("   O_| ")
                print("  /|\  ")
                print("  / \  ")
                break


name = input("Enter your name: ")
print("Welcome", name)
print("------------------\n"+"Try to guess the names in less than 10 attempts...\n")
hangman()
print()
