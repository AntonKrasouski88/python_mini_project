# Name of the game is hangman
import random, sys

# Greate variable with words
word_list = ['abruptly', 'galaxy', 'matrix', 'python', 'jackpot', 'hockey', 'ballet', 'zigzagging', 'welcome', 'zombie', 'wizard', 'keyboard']

def get_word(arr):
   word = arr[random.randrange(len(word_list) - 1)]
   return word


def display_hangman(tries):
   stages = [  # final state: head, torso, both arms, both legs
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # head, torso, both arms, one leg
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # head, torso, both arms
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # head, torso and arm
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # head and torso
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # head
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # initial state
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
   print(stages[tries])


def check_choice_user (choice):
   
   for c in choice:
      if ord(c) < 65 or ord(c) > 122:
         return False
   
   return True
   
def play (word):
   world_completion = '_' * len(word) # a string containing _ characters for each letter of the intended word
   guessed = False                    # signal label
   guessed_letters = []               # list of already named letters
   guessed_words = []                 # list of already named words
   tries = 6                          # number of attempts
   
   print("Let's play the guessing of words!")
   display_hangman(tries)             # display the current state of the game with the initial number of permissible misses
   
   while tries > 0:
      print(world_completion)         # display the initial words
      choice_user = input('Enter the letter or word: ').strip()
      flag = check_choice_user(choice_user)
      
      if not flag:
         print('The entered character is not a letter')
         
      else:
         if len(choice_user) == 1:
            if choice_user in guessed_letters:
               print('This letter has already been selected earlier. Be careful!')
               tries -= 1
            else:
               if choice_user in word:
                  for i in range(len(word)):
                        if word[i] == choice_user:
                           world_completion = world_completion[:i] + word[i] + world_completion[i + 1:]
                  guessed_letters.append(choice_user)
               else:
                  guessed_letters.append(choice_user)
                  tries -= 1
         else:
            if choice_user in guessed_words:
               print('This word has already been selected earlier. Be careful!')
               tries -= 1
            else:
               if choice_user == word:
                  guessed = True
                  break
               else:
                  guessed_words.append(choice_user)
         
   if guessed:
      print('Congratulations, you guessed the word! You win!')
   elif tries == 0:
      display_hangman(tries)
      print(f'You lose. Correct word: {word}')
   else:
      display_hangman(tries)
      


play(get_word(word_list))

while True:
   flag = input('Do you want to play again? Please enter: Y(YES) or N(No) ');
   if flag.upper() == 'Y':
      play(get_word(word_list))
   else:
      sys.exit()
