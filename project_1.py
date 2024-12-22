import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, please try again.")

max_score = 21
player_scores = [0 for _ in range(players)]

while True:
    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "turn has just started!\n")
        print("Your total score is:", player_scores[player_idx])

        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll? (y/n)? ")
            if should_roll.lower() == "n":
                break
            elif should_roll.lower() == "y":
                value = roll()
                print("You rolled a:", value)
                
                if value == 1:
                    print("You rolled a 1! Turn done!")
                    current_score = 0
                    break
                else:
                    current_score += value
        
        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

        if player_scores[player_idx] >= max_score:
            print("Player number", player_idx + 1, "is the winner with a score of:", player_scores[player_idx])
            exit()