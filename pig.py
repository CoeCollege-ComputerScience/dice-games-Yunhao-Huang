import random

def pig():
    totals = [0, 0]  
    current_player = 0  
    current_score = 0

    while True:
        print(f"\nPlayer {current_player + 1}'s turn")
        roll = random.randint(1, 6)
        print(f"Rolled: {roll}")
        if totals[current_player] + current_score>= 100:
            print(f"Player {current_player + 1} wins!")
            break

        if roll == 1:
            print("Oops! Rolled 1, no score, switch player.")
            current_score = 0
            current_player = 1 - current_player  
            continue

        current_score += roll
        print(f"Current score this turn: {current_score}, Total: {totals[current_player]}")

        choice = input("1 to continue, 2 to hold: ")
        if choice == "2":
            totals[current_player] += current_score
            print(f"Player {current_player + 1} holds. Total: {totals[current_player]}")
            if totals[current_player]>= 100:
                print(f"Player {current_player + 1} wins!")
                break
            current_score = 0
            current_player = 1 - current_player
        elif choice != "1":
            print("Invalid input, please try again.")

pig()