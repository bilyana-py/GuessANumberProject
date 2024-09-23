import random


def main():
    computer_number = random.randint(1, 100)
    counter = 0

    print('You have only 10 tries to guess the number')
    while counter <= 10:
        player_input = input("Guess the number (1-100): ")

        if not player_input.isdigit():
            print("Invalid input. Try again...")
            counter += 1
            continue

        player_number = int(player_input)
        counter += 1

        if player_number == computer_number:
            print('You guess it! \n Do you want to start again or go to the next level? \n If yes, type "yes", '
                  'if no, type "no". If you want to go to the next level, type "next level".')
            yes_or_no = input()
            if yes_or_no == 'yes':
                main()
            elif yes_or_no == 'next level':
                computer_number = random.randint(1, 200)
                counter = 0

                print('You have only 10 tries to guess the number')
                while counter <= 10:
                    player_input = input("Guess the number (1-200): ")

                    if not player_input.isdigit():
                        print("Invalid input. Try again...")
                        counter += 1
                        continue

                    player_number = int(player_input)
                    counter += 1

                    if player_number == computer_number:
                        print('You guess it! \n Do you want to start again? \n If yes, type "yes", if no, type "no".')
                        yes_or_no = input()
                        if yes_or_no == 'yes':
                            main()
                        else:
                            exit()
                    elif player_number > computer_number:
                        print('Too high!')
                    elif player_number < computer_number:
                        print('Too low!')
            else:
                exit()
        elif player_number > computer_number:
            print('Too high!')
        elif player_number < computer_number:
            print('Too low!')

main()
print('You do not have any more tries! \n Do you want to try again?')
yes_or_no = input()
if yes_or_no == 'yes':
    main()
else:
    exit()
