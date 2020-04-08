#! python3
from random import randint



def input_h1():
    while True:
        rawup = input('Enter letter: ').upper()
        if len(rawup) == 1 and rawup.isalpha() and not rawup in display and not rawup in wrong_letters:
            return rawup
        else:
            print('Invalid input. Please enter only one letter that you haven\'t tried before.\n')

def input_h2():
    while True:
        rawup = input('<yes/no> ').upper()
        if rawup == 'YES' or rawup == 'NO':
            return rawup
        else:
            print('Invalid input. Enter only "yes" or "no".')

# random word picker
def r_word(wordbankfile='sowpods.txt'):
    with open(wordbankfile, 'r') as f:
        word_list = f.readlines()
        striped_list = []
        for line in word_list:
            striped_list.append(line.strip())
    size = len(striped_list)
    return striped_list[randint(0, (len(word_list) - 1))]


def drawgame():
    show_display = ' '.join(display)
    hangman_dict = {6:r'''
 _____ 
|    $ 
|   /|\
|   / \ ''', 5:r'''
 _____ 
|    0 
|   /|\
|    |  ''', 4:r'''
 _____ 
|    0 
|   /|\
|       ''', 3:r'''
 _____ 
|    0 
|   / \
|       ''', 2:'''
 _____ 
|    0 
|    | 
|       ''', 1:'''
 _____ 
|    0 
|      
|       ''', 0:'''
 _____ 
|      
|      
|       '''}
    print(hangman_dict[to_hang] + 'Secret Word: ' + show_display + '\n' + message + '\n')
    


# global scope -----------------------
print('''
===================================================
Welcome to the Hangman Game!
===================================================
Your objective is to guess the secret word spelling
letter by letter. But, caution! If you spell six
letters wrong, you lose!''')


still_playing = True
while still_playing:
    
    word = r_word()
    display = ['_']*len(word)
    to_hang = 0
    wrong_letters = []
    message = ''

    drawgame()

    player_not_won = True
    player_not_dead = True
    while (player_not_won and player_not_dead):

        player_letter = input_h1()
        if player_letter in word:
            index = 0
            for letter in word:
                if letter == player_letter:
                    display[index] = player_letter
                    message = f'Great! "{player_letter}" is found.'
                index += 1

        else:
            to_hang += 1
            wrong_letters.append(player_letter)
            message = f'Letter "{player_letter}" not found in the secret word.'

        drawgame()

        if to_hang >= 6:
            player_not_dead = False
            print('You tried 6 wrong letters and lost! Wrong letters: ' + ', '.join(wrong_letters) + '.')
            print(f'The secret word was "{word}".')

        if ''.join(display) == word:
            player_not_won = False
            print(f'You\'ve won! The secret word is "{word}".')


    print('\n\n\nWant to play again?')
    if input_h2() == 'YES':
        pass
    else:
        still_playing = False
