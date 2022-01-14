import random
from re import A
from secrets import choice


def main():
    choices = ["rock", "paper", "scissors"]
    opponent = random.choice(choices)
    userChoice = input(
        f"Rock Paper opponent! Select an option below.\n{choices[0]},{choices[1]}or {choices[2]} \n").lower()
    try:
        if userChoice in choices:
            # Play game
            if userChoice == "rock" and opponent == "scissors":
                print(f'Congragulations you beat me! I chose {opponent}')
            elif userChoice == "rock" and opponent == "paper":
                print(f"Ha ha I win, I chose {opponent}")
            elif userChoice == "scissors" and opponent == "paper":
                print(f"Ah you beat me, I chose {opponent} ")
            elif userChoice == "scissors" and opponent == "rock":
                print(f"Rock Beats scissors! I chose {opponent} for a reason!")
            elif userChoice == "paper" and opponent == "rock":
                print(f"You beat me! I chose {opponent}")
            elif userChoice == "paper" and opponent == "scissors":
                print(f"I chose {opponent} You loose!")
            elif userChoice == opponent:
                print(
                    f"Looks like I chose {userChoice} as well! Let's re-draw!")
                (main())
        elif userChoice not in choices:
            print("That's not a selection!")
            main()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
