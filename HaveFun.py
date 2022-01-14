import random


def main():

    def playGame(correctNum, maxTries):
        guess = input("What do you think the number is?")

        if int(guess) == int(correctNum):
            return True
        elif maxTries <= 0:
            print(
                f"You ran out of guesses! The correct number was {correctNum} good luck next time!")

        elif guess != correctNum:
            print(
                f'{guess} Wasn\'t the correct number! You have {maxTries} tries left!')
            return False

    try:
        x = input("What is the starting range that you'd like?")
        y = input("What is the ending range you'd like?")
        correctNum = random.randint(int(x), int(y))
        maxTries = 3
        for x in range(maxTries):
            maxTries -= 1
            c = playGame(correctNum, maxTries)
            if c == True:
                print(
                    f"Congrats! You selected the right number! The number was {correctNum}!")
                break

    except ValueError:
        print("That is not a number.")
        main()


if __name__ == "__main__":
    main()
