from random import choice 
import os

def changing_words(last_word, letter, letter_index):
    new_word = list(last_word)
    new_word[letter_index] = letter
    new_word = ''.join(new_word)
    return new_word


def choosing_word():
    global hide_word
    global word_line
    global used_words
    global attempts
    letter_index = 0
    chosen_word = ''
    while chosen_word == '':
        try:
            chosen_word = str(input('chose a letter:'))
            chosen_word = chosen_word.upper() 
            assert chosen_word == ('A' <= chosen_word)  or (chosen_word <= 'Z') and chosen_word.isalpha()
        except:    
            chosen_word = ''
            os.system("clear")
            print('please choose only one letter from A to Z \n')
            continue
    if chosen_word in used_words:
        os.system("clear")
        print('you already used that letter\n')
        attempts -= 1 
    elif not chosen_word in hide_word:
        os.system("clear")
        print(choice(mistake) + ', try again\n')
        attempts -= 1
    else:
        used_words.append(chosen_word)
        while chosen_word in hide_word:
            letter_index = hide_word.find(chosen_word)
            word_line = changing_words(word_line, chosen_word, letter_index)
            hide_word= changing_words(hide_word, "*", letter_index)
            os.system("clear")
            print('Good! you find one\n')


def hangman_game():   
    global hide_word
    global word_line 
    global points
    global attempts
    hide_word = choice(list_words)
    hide_word = hide_word.upper() 
    word_line = "_" * len(hide_word)
    while attempts >=1:
        print('Find this word: \n' + word_line + '\n\nattemps left: ' + str(attempts))
        if '_' in word_line:
            choosing_word()
        else:
            points +=1
            os.system("clear")
            print('\^O^/ ---' + word_line + '--- |@w@|\n')
            print('you did it!!! ^u^ \n')
            print('attemps used: ' + str(10 - attempts))           
            break
    if attempts == 0:
        print('no more attempts... sorry morry \n')


def game_over():
    print('Game Over \n') 
    show_points()
    print('Thanks for playing') 
    again == 0


def show_points():
    print('Your score is: ' + str(points) + '\n')


def gameboot(): 
    global attempts  
    global used_words
    coins = 0
    while again == 1:
        show_points()
        used_words = []
        try:
            coins = int(input('Do yo want to play?\nYes = 1 / No = 0: ')) ###Verificacion
            assert coins == 1 or 0, "wrong input <_< U\n"
        except:
            continue    
        if coins == 1:
            attempts += 10
            hangman_game()
        elif coins == 0:
            game_over()

 
        

        


list_words = ['memekyun', 'panochon', 'mamachona', 'papikyun', 'refresco']
points = 0
again = 1
attempts = 0
coins = 0
used_words = []
hide_word = ''
word_line = ''
mistake = ['No', 'Nope', 'Not even close', 'Good try, but nop']

if __name__ == '__main__':
    gameboot()
    
    