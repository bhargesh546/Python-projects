import random, sys

def main():
    print("ROCK 👊, PAPER 🤚, SCISSORS ✌️")

    wins = 0
    losses = 0
    ties = 0

    while True:
        print(f"Wins: {wins}  Losses: {losses}  Ties: {ties}")
        p_move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ").lower()
        c_move = random.choice(["r", "p", "s"])
        
        if p_move == 'q':
            sys.exit("Thanks for playing")          # Quit the program.
        elif p_move not in ['r', 'p', 's']:
            print("Type one of r, p, s, or q.") 
            continue                                # go back to the start of the while loop                               
        
        result = rps_game(p_move, c_move)

        if result == "win":
            wins += 1
        elif result == "loss":
            losses += 1
        else:
            ties += 1

def rps_game(player_move, computer_move):

    # Display what the player chose:
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    if computer_move == 'r':
        print('ROCK')
    elif computer_move == 'p':
        print('PAPER')
    elif computer_move == 's':
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if player_move == computer_move:
        print("It's a tie!")
        return "tie"
    elif (player_move == 'r' and computer_move == 's') or (player_move == 'p' and computer_move == 'r') or \
            (player_move == 's' and computer_move == 'p'):
        print('You win!')
        return "win"
    else:
        print('You lose!')
        return "loss"


if __name__ == "__main__":
    main()