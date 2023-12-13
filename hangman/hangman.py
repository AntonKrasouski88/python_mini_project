# Name of the game is hangman
import random

# Greate variable with words
word_list = ['abruptly', 'galaxy', 'matrix', 'python', 'jackpot', 'hockey', 'ballet', 'zigzagging', 'welcome', 'zombie', 'wizard', 'keyboard']

def get_word(arr):
   word = arr[random.randrange(len(word_list) - 1)]
   return word.upper()

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
   return stages[tries]

def check_choice_user (choice):
   punctuation = '!#$%&*+-=?@^_.,'
   flag = False
   for c in choice:
            for l in punctuation:
               if c == l:
                  flag = True 
   if flag:
       print('Error: A symbol that is not a letter is introduced')

   return flag

def check_repeated_words (list_word, word):
   flag = False

   for w in list_word:
       if w == word:
           flag = True

   return flag

def check_repeated_letter (list_letter, letter):
   flag = False

   for l in list_letter:
      if l == letter:
         flag = True

   return flag
   
def play (word):
   world_completion = '_' * len(word) # string, has symbols _ 
   guessed = False
   guessed_letters = []
   guessed_word = []
   tries = 6
   
   print("Let's play the guessing of words!")
   display_hangman(tries) # display the current state of the game with the initial number of permissible misses
   print(world_completion) # display the initial words

   while tries > 0:
      flag = True
      choise_user = ''

      while flag:
         choice_user = input('Enter the letter or word: ' ).strip()
         flag = check_choice_user(choice_user)

      """ if len(choise_user) == 1:
         guessed_letters.append(choise_user)
      else:
         guessed_word.append(choise_user) """
      


