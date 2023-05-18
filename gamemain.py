from random import randint

CS = 0  # computer_score
PS = 0  # player_score

while True:
    valid_input = False
    while not valid_input:
        user_input = input("Rock(1), Paper(2), Scissors(3)! (Enter 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        if user_input.isdigit():
            In = int(user_input)
            if In in [1, 2, 3]:
                valid_input = True
                randnum = randint(1, 3)

                if In == randnum:
                    CS = CS
                    PS = PS
                elif In == 3 and randnum == 2:  # Scissor vs Paper
                    PS += 1
                elif In == 2 and randnum == 3:  # Paper vs Scissor
                    CS += 1
                elif In == 3 and randnum == 1:  # Scissor vs Rock
                    CS += 1
                elif In == 1 and randnum == 2:  # Rock vs Paper
                    CS += 1
                elif In == 1 and randnum == 3:  # Rock vs Scissor
                    PS += 1
                elif In == 2 and randnum == 1:  # Paper vs Rock
                    PS += 1

                print('Computer:', randnum, ', Player:', In)
                print("Computer's Score:", CS, ", Player's Score:", PS)
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        else:
            print("Invalid input. Please enter a number.")

    if user_input.lower() == 'q':
        break

print("Final Score: Computer:", CS, ", Player:", PS)
if CS == PS:
    print('It is a tie.')
elif CS > PS:
    print('Computer wins.')
else:
    print('Player wins.')
