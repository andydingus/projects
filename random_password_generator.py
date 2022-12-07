import random, sys, os, pyperclip

# No lowercase l, uppercase I and O
LETTERS_LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
LETTERS_UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F' , 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['2','3','4','5','6','7','8','9']

SYMBOLS = [LETTERS_LOWERCASE, LETTERS_UPPERCASE, NUMBERS]
password = f'{random.choice(SYMBOLS[random.randint(0,2)])}{random.choice(SYMBOLS[random.randint(0,2)])}{random.choice(SYMBOLS[random.randint(0,2)])}{random.choice(SYMBOLS[random.randint(0,2)])}{random.choice(SYMBOLS[random.randint(0,2)])}{random.choice(SYMBOLS[random.randint(0,2)])}{random.choice(SYMBOLS[random.randint(0,2)])}{random.choice(SYMBOLS[random.randint(0,2)])}'
pyperclip.copy(password)
print(f'Here\'s a password: {password} \nThe password has been copied to your clipboard')
def main():
    generating = True
    while generating:
        generateNewPassword = input('Get a new password? \n Press y if you want one, n to stop.')
        if generateNewPassword == 'y':
            os.system('cls')
            newPassword = f'{random.choice(SYMBOLS[random.randint(0,2)])}{random.choice(SYMBOLS[random.randint(0,2)])}{random.choice(SYMBOLS[random.randint(0,2)])}{random.choice(SYMBOLS[random.randint(0,2)])}{random.choice(SYMBOLS[random.randint(0,2)])}{random.choice(SYMBOLS[random.randint(0,2)])}{random.choice(SYMBOLS[random.randint(0,2)])}{random.choice(SYMBOLS[random.randint(0,2)])}'
            pyperclip.copy(newPassword)
            print(f'Here\'s a new password: {newPassword} \nThe password has been copied to your clipboard')         
        elif generateNewPassword == 'n':
            sys.exit()
            
main()