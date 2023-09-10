# Caesar's cipher: The program is capable of encrypting and decrypting text in accordance with the Caesar algorithm

# We request the following data from the user: direction, language, shift_step
direction = input("Direction [encryption: enter 'E' or decryption: 'D']: ")
language = input("Alphabet language [Russian: enter 'R' or English: 'E']: ")
shift_step = int(input("Shift step (shift right): "))
text = input("Enter text to encrypt (decrypt): ")

# Non-alphabetic characters - punctuation marks, spaces, numbers - do not change
punctuation = '!#$%&*+-=?@^_.,'

en = [97, 122]  # English characters code in the Unicode character table: 97 - 122
# Russian characters code in the Unicode character table: 1072 - 1103
ru = [1072, 1103]


def encryption_str(text, lang, shift):
    s = ''  # Create a variable into which we will transfer the encrypted string

    for c in text:  # Let's create a loop that will shift each character
        # Non-alphabetic characters - punctuation marks, spaces, numbers - do not change
        if punctuation.find(c) != -1 or c == ' ':
            s += c
            continue

        # Condition in case of exceeding the maximum value for characters
        if ord(c.lower()) + shift > lang[1]:
            a = (ord(c.lower()) + shift) - lang[1]
            s += chr(lang[0] - 1 + a)
        else:
            s += chr(ord(c.lower()) + shift)

    return s.capitalize()


def decryption_str(text, lang):
    s = ''  # A loop that outputs all shifts according to the number of letters in the alphabet
    arr = []
    for i in range(1, lang[1] - lang[0] + 2):

        for c in text:
            # Non-alphabetic characters - punctuation marks, spaces, numbers - do not change
            if punctuation.find(c) != -1 or c == ' ':
                s += c
                continue
            # Condition in case of exceeding the maximum value for characters
            if ord(c.lower()) - i < lang[0]:
                a = lang[0] - (ord(c.lower()) - i)
                s += chr(lang[1] + 1 - a)
            else:
                s += chr(ord(c.lower()) - i)

        arr.append(s.capitalize())
        s = ''

    return arr


# Conditions for processing user data (direction, language)
if direction.upper() == 'E':
    if language.upper() == 'E':
        print(encryption_str(text, en, shift_step))
    else:
        print(encryption_str(text, ru, shift_step))
else:
    if language.upper() == 'E':
        print(*decryption_str(text, en), sep='\n')
    else:
        print(*decryption_str(text, ru), sep='\n')
