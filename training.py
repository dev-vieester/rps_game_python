import sys
from enum import Enum
from random import  choice

def rps(player_name = 'PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_name
        nonlocal  player_wins
        nonlocal python_wins
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSOR = 3

        player_choice = input(f"\n{player_name}, please enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

        if player_choice not in ['1', '2', '3']:
            print(f"{player_name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(player_choice)

        computer_choice = choice('123')

        computer = int(computer_choice)

        print(f'\n{player_name}, you chose  {RPS(player).name} .')
        print(f'Python chose {str(RPS(computer)).replace('RPS.','').title()} .\n')
        def decide_winner(player, computer):
            nonlocal player_name
            nonlocal  player_wins
            nonlocal  python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {player_name}, you win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {player_name}, you win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {player_name}, you win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {player_name}...😔"

        game_result = decide_winner(player, computer)
        print(game_result)
        nonlocal  game_count
        game_count += 1
        print(f'\nGame count: {game_count}')
        print(f'\n{player_name}, you wins: {player_wins}')
        print(f'\nPython wins: {python_wins}')

        print(f"\nPlay again, {player_name}")

        while True:
            play_again = input('\nY for Yes or \nQ fo Quit\n')
            if play_again.lower() not in ['y', 'q']:
                continue
            else:
                break

        if play_again.lower() == 'y':
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉")
            print(f"Thank you {player_name} for playing!\n")
            sys.exit("Bye! 👋")
    return play_rps



if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Provide a personalized game experience'
    )

    parser.add_argument('-n', '--name', metavar='name', required=True, help='Player name')

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()

