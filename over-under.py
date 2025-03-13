import random

def overunder():
    totals = [0, 0]  
    current_player = 0  
    num1 = 0
    num2 = 0
    while True:
        if totals[current_player] == 6:
            print(f"Player {current_player + 1} wins!")
            break
        print(f"\nPlayer {current_player + 1}'s turn")
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        dice_3 = random.randint(1, 6)
        num1 = dice_1 + dice_2 + dice_3
        print(f"Rolled: {num1}")
        choice = input("1=over, 2=under: ")
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        dice_3 = random.randint(1, 6)
        num2= dice_1 + dice_2 + dice_3
        print(f"Second roll: {num2}")
        if choice == "1":
            if num2 > num1:
                print(f"Player {current_player+1}, You win!")
                totals[current_player] += 1
                print(f"Player {current_player+1} score: {totals[current_player]}")
            else:
                print(f"Player {current_player+1}, You lose!")
        elif choice == "2":
            if num2 < num1:
                print(f"Player {current_player+1}, You win!")
                totals[current_player] += 1
                print(f"Player {current_player+1} score: {totals[current_player]}")
            else:
                print(f"Player {current_player+1}, You lose!")
        else:
            print("Invalid input, please try again.")
        current_player = 1 - current_player


overunder()