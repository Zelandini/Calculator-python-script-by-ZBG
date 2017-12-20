# <===========================================>#
# This program made by Zelandini Borromeu Guterres
# If there's any question ask me via:
# zelandiniduarte@gmail.com

# Thank for downloading # hastag i don't win money from this  
# Novince programmer
#PEACE!!!

from colorama import Fore  # Not necessary can be deleted

tries = 0


# Introduction of the script
def intro():
    print(" ")
    print("---Calculator---")
    print(Fore.GREEN + "\nby ZBG")  # <---- Delete Fore if you don't have colorama can be downloaded from pip
    print(Fore.BLACK, "\n----Options----")  # <--- Also this!!!
    print('Enter "add" two add to numbers')
    print('Enter "subtract" to subtract two numbers')
    print('Enter "multiply" to multiply two numbers')
    print('Enter "divide" to divide to numbers')
    print('Enter "quit" to end the program')
    main()  # <--- It goes to main


# The main script
def main():
    global tries
    while True:  # Loop if input not in intro

        userInput = input("\n>").lower()

        if userInput == "add":  # If input is add it runs this part
            num1 = int(Num1("\nEnter first number:"))  # Goes to Num1
            print("--------------")
            num2 = int(Num2("Enter second number:"))  # Goes to Num2
            print(num1, "+", num2, "=", addTwoN(num1, num2))
            tries += 1
            restart()  # Goes to restart

        elif userInput == "subtract":  # If input is subtract it runs this part
            num1 = int(Num1("\nEnter first number:"))
            num2 = int(Num2("Enter second number:"))
            print(num1, "-", num2, "=", subTwoN(num1, num2))
            tries += 1
            restart()

        elif userInput == "multiply":  # If input is multiply it runs this part
            num1 = int(Num1("\nEnter first number:"))
            num2 = int(Num2("Enter second number:"))
            tries += 1
            mulTwoN(num1, num2)
            restart()

        elif userInput == "divide":  # If input is divide it runs this part
            num1 = int(Num1("\nEnter first number:"))
            num2 = int(Num2("Enter second number:"))
            tries += 1
            divTwoN(num1, num2)
            restart()

        elif userInput == "quit":  # If input is quit it runs this part
            quiting()  # Goes to function quit

        else:
            print("Unknown input. Try again")  # The reason to LOOP!


def quiting():  # A funny way to end. That is why i use the var "trie" LOL
    if tries == 1:
        print("Thank for using!")
        quit()  # Not a function it's a code to end the program

    elif tries >= 2:
        print("Thank you for using, I love it! ")

    else:
        print("You haven't use it once!")
        quit()


def Num1(string):  # The method runs if input is NUMERIC else it LOOPS
    Ask1 = input(string)
    while not Ask1.isnumeric():  # See LOOPS when input is not numeric
        print("\n*******************************")
        print("Invalid input. !Please try again!")
        print("*********************************")
        Ask1 = input("\n" + string)

    return Ask1  # If it is runs it returns the value to var "num1" on main() function


def Num2(string):  # Same work as Num1 but for var "num2"
    Ask2 = input(string)
    while not Ask2.isnumeric():
        print("\n*******************************")
        print("Invalid input. !Please try again!")
        print("*********************************")
        Ask2 = input("\n" + string)

    return Ask2  # return value to var "num2" on main() function


def addTwoN(num1, num2):  # function to add numbers
    print("-----------")
    return num1 + num2  # it returns the value to main()


def subTwoN(num1, num2):  # function to subtract numbers
    print("-----------")
    return num1 - num2  # it returns the value to main()


def mulTwoN(num1, num2):  # function to multiply numbers
    print("-----------")
    return num1 * num2  # it returns the value to main()


def divTwoN(num1, num2):  # function to divide numbers
    print("-----------")
    return num1 / num2  # it returns the value to main()


def restart():  # this function ask user if they want to restart the program
    print("\nDo you want to restart?")
    while True:
        question = input(">").lower()
        if question in ("yes", "y"):
            print("\nRestarting....")
            intro()

        if question in ("no", "n"):
            quiting()

        else:
            print("Unknown input. Try again!")


intro()  # from the beginning runs this
