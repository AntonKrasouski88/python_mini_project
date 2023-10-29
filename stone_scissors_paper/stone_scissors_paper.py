#This game: stone or scissors or paper
from random import randint

#This variables save quantity wins, losses, ties
wins = 0 
losses = 0
ties = 0

#There are possible options in this list
options = ['rock', 'paper', 'scissors']
flag = True

print("Hello. This game is called 'rock, paper, scissors'")

#This function cheks the user's selection
def check_choice():
    while True:
        choice = input('You need to choose: rock(R), paper(P), scissors(S) or exit(E)').upper().strip()
        
        if choice == 'R':
            return options[0] 
        if choice == 'P':
            return options[1]
        if choice == 'S':
            return options[2]
        if choice == 'E':
            return 'E'
        
        print('Error: incorrect choice')


#This function compares selecting a user with a computer
def compare_choices(user, pc):
    print(f'Your choice is {user} and pc choice is {pc}')

    if user == pc:
        print('Tie!')
        return 't'
    if user == options[0] and pc == options[2]:
        print('You win!')
        return 'w'
    if user == options[1] and pc == options[0]:
        print('You win!')
        return 'w'
    if user == options[2] and pc == options[1]:
        print('You win!')
        return 'w'
    else:
        print('You lose!')
        return 'l'

while flag:
    #This variable stores the computer choice
    choice_pc = options[randint(0, 2)]

    #This variable stores the user's choice
    choice_user = check_choice()
    
    #Program exit check
    if choice_user == 'E':
        flag = False
        break

    result = compare_choices(choice_user, choice_pc)

    #Check result and increase variable
    if result == 'w':
        wins += 1
    if result == 'l':
        losses += 1
    if result == 't':
        ties += 1
    
    print(f'Wins: {wins}, losses: {losses}, ties: {ties}')