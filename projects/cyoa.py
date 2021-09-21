"""Project 0: Creating my own adventure using the Monty Hall Problem."""

__author__ = "730489843"


from random import randint

points: int
player: str
strategy_unlocks: int
runs: int
wins: int
description: int

HAPPY_FACE: str = "\U0001f600"
SAD_FACE: str = "\U0001F641"


def correct_door() -> int:
    """returns the door number containing the prize"""
    door_no = randint(1, 3)
    return door_no


def incorrect_door(correct : int, choice : int) -> int:
    """returns an incorrect door in 1st step of Monty Hall Problem"""
    if correct == choice:
        if correct == 1:
            return 2
        else:
            if correct == 2:
                return 3
            else:
                return 1
    else:
        return 1 + 2 + 3 - correct - choice


def rules(points: int) -> int:
    """Returns the rules and strategies which can be used to win the game."""
    global strategy_unlocks, description
    rules_1 = int(input(
f'''
{player}, enter 1 to read the description of the game. You will earn one point if you enter 1!
Enter 2 to read a few strategies to perform better at the game. However, BEWARE! YOU WILL LOSE 1 POINT!
Enter 3 to exit and return to the game.
'''
    ))
    if rules_1 == 1:
        print(
'''
The Monty Hall problem is a classic game theory problem, where the player has to choose to open one of three closed doors to win a prize.
The host knows which door has the prize behind it, and will choose to open an incorrect door (it cannot be the one the player chose).
The player will then be given the option to either stay with their choice or switch to the other closed door.
Their final decision could be the only thing in their way of winning a grand prize!
Start playing the game to earn one free point, but feel free to use the 'Strategy' option at the cost of one point!
'''
        )
        points += 1
        description += 1
        print(f"{player}, your total points are: {points}")
    else:
        if rules_1 == 2:
            print(
'''
Strategy - There is always a higher probabilty of the player winning if they choose to switch their decision to the other unopened door (probability of winning is 2/3 when they switch, but remains 1/3 when they do not switch!)
'''
            )
            strategy_unlocks += 1
            points -= 1
            print(f"{player}, your total points are: {points}")
    return points




def simulate() -> None:
    """Simulates a run of Monty Hall."""
    global player, points, runs, wins
    runs += 1
    choice = int(input(f"Okay, {player}! You have three doors: 1, 2 and 3. Choose your lucky door!"))
    points += 1
    jackpot = correct_door()

    # open an incorrect door
    incorrect = incorrect_door(jackpot, choice)
    print(f"Let's open door {incorrect}. Oh, but this is pure garbage!")
    print("Now you have two doors. Would you like to stay with your original door or switch?")
    print("Enter 1 to stay")
    print("Enter 2 to switch")
    switch_response = int(input())
    won : bool = False
    if switch_response == 1:
        # chose to stay
        if choice == jackpot:
            won = True
        else:
            won = False
    else:
        # chose to switch
        if choice == jackpot:
            won = False
        else:
            won = True
    
    if won:
        points += 2
        wins += 1
        print(f"Congrats! {HAPPY_FACE} You win! The correct door was {jackpot}!")
    else:
        print(f"Oops! Tough luck! {SAD_FACE} The correct door was {jackpot}")
            

def greet() -> None:
    """Greets the player as soon as the program is run."""
    global player
    print("Welcome to the Monty Hall Problem!")
    player = input("Enter your name to begin: ")
    return None

def main() -> None:
    """Main function that runs the whole game."""
    global points, runs, wins, strategy_unlocks, description
    greet()
    print(f"Welcome to the Monty Hall Problem {player}!")
    points = 0
    runs = 0
    wins = 0
    strategy_unlocks = 0
    choice = -1     # Any value other than 3 is ok here
    description = 0
    while choice != 3:     
        print("-------------")
        print("Enter 1 to play the game once")
        print("Enter 2 to read the rules of the game")
        print("Enter 3 to exit the game")
        choice = int(input())
        if choice == 1:
            simulate()
            print(f"Well done {player}, you scored {points} points!")
        if choice == 2:
            points = rules(points)
    print(f"Adios {player}! You played well and scored {points} points!")
    print("Here are a few more stats for you:")
    print(f"You played {runs} times and won {wins} times!")
    print(f"You unlocked the strategy {strategy_unlocks} times")
    print(f"You read the description {description} times!")
    return None

if __name__ == "__main__":
    main()