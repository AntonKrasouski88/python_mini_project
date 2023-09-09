# Sucure password generator
import random  # Connect the module random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

num_of_pass = int(input('How many passwords are needed to generate?: ' ))
len_of_pass = int(input('What is the length of one password needed?: '))
incl_num = input('Should the numbers 0123456789 be included? [YES: enter "Y", NO: enter "N"]: ').strip()
incl_uppercase = input('Should uppercase ABCDEFGHIJKLMNOPQRSTUVWXYZ be included? [YES: enter "Y", NO: enter "N"]: ').strip()
incl_lowercase = input ('Should lowercase abcdefghijklmnopqrstuvwxyz be included? [YES: enter "Y", NO: enter "N"]: ').strip()
incl_sym = input('Should the characters !#$%&*+-=?@^_ be included? [YES: enter "Y", NO: enter "N"]: ').strip()
exclud_char = input('Exclude different characters il1Lo0O? [YES: enter "Y", NO: enter "N"]: ').strip()

	
if incl_num.lower() == 'y':
	chars += digits
if incl_uppercase.lower() == 'y':
	chars += lowercase_letters
if incl_lowercase.lower() == 'y':
	chars += uppercase_letters
if incl_sym.lower() == 'y':
	chars += punctuation
if exclud_char.lower() == 'y':
	for c in 'il1Lo0O':
		chars = chars.replace(c, '')


def generate_password(length, chars):
	password = ''
	ln = len(chars)
	for _ in range(length):
		password += chars[random.randrange(ln)]
	return password


for _ in range(num_of_pass):
	generate_password(len_of_pass, chars) 
