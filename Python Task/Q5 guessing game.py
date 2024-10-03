total_points = 0

for stage in range(1, 4):
    if stage == 1:
        secretNumber=5
        print("Stage 1: Guess the number between 1 and 10")
    
    elif stage == 2:
        secretNumber=8
        print("Stage 2: Guess the number between 1 and 20")
    
    elif stage == 3: 
        secretNumber=30
        print("Stage 3: Guess the number between 1 and 30")

    points_awarded = 0
    for attempt in range(1, 6):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess == secretNumber:
            if attempt == 1:
                points_awarded = 100
            elif attempt == 2:
                points_awarded = 75
            elif attempt == 3:
                points_awarded = 50
            elif attempt == 4:
                points_awarded = 25
            else:
                points_awarded = 10
            print("Your guess is correct! Moving to the next level.")
            total_points += points_awarded
            break  # Move to the next stage
        elif guess > secretNumber:
            print("Your guess is greater than the secret number.")
        else:
            print("Your guess is less than the secret number.")
    
    if points_awarded == 0:
        print("Game Over, You Lose the Game.")
        break  
else:
    print(f"You won the game with {total_points} points!")
