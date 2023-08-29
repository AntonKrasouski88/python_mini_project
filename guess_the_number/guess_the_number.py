# Game: guess the number
import random  # Connect the module random

flag = True


def get_right_border():  # Set the right border of a random number
    while True:
        print('Enter a right border to randomly select a number')
        right_border = input()
        if right_border.isdigit() and int(right_border) > 1:
            return int(right_border)


def is_valid(data, right_num):  # Check that the data is the integer number
    return data.isdigit() and 0 < int(data) <= right_num and 0 == float(data) - int(data)


def continue_game():  # Checking the introduced symbol
    while True:
        print('Do you want to repeat the game? YES: enter "Y", NO: enter "N"')
        c = input()
        if c.lower() == 'y':
            return True
        elif c.lower() == 'n':
            return False
        else:
            print('Error, you need to choose "Y"(YES) or "N"(NO)')


def guess_the_number():
    print('Hello, Welcome to the number guess')
    num_right = get_right_border()  # Right border
    num_random = random.randint(1, num_right)  # Generate a random number
    count = 1  # The counter of attempts

    while True:

        print(f'Enter the number from 1 to {num_right}')
        num_user = input()  # The user introduces the meaning

        if not is_valid(num_user, num_right):  # Check the data
            print(f'Or maybe we’ll still introduce an integer from 1 to {num_right}?')
            continue

        n = int(num_user)  # Transform the data to the number

        if n < num_random:  # Folding the number of the user with a random number
            print('Your number is less than the mystery, try it again')
            count += 1
        elif n > num_random:
            print('Your number is more than the mystery, try it again')
            count += 1
        else:
            print('You guessed, congratulations!')
            print(f'You needed {count} attempts.')
            break

    print('Thank you for playing in a numerical guess. See you...')

    return continue_game()


while flag:
    flag = guess_the_number()
