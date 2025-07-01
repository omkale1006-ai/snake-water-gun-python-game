import random

def check_win(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "s" and computer == "w") or \
         (player == "w" and computer == "g") or \
         (player == "g" and computer == "s"):
        return "Player"
    else:
        return "Computer"

def main():
    print("Welcome to Snake-Water-Gun Game!")
    print("Choose: s for Snake, w for Water, g for Gun")

    player = input("Your choice (s/w/g): ").lower()
    if player not in ['s', 'w', 'g']:
        print("Invalid input! Choose only 's', 'w' or 'g'")
        return

    computer = random.choice(['s', 'w', 'g'])

    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")

    winner = check_win(player, computer)

    if winner == "Tie":
        print("It's a Tie!")
    elif winner == "Player":
        print("🎉 You Win!")
    else:
        print("😢 Computer Wins!")

# Run the game
main()
