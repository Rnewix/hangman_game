from random import choice 

def choosing_word():
    print(word_line)
    chosen_word = str(input('chose a letter'))   ###Verificacion
    count= hide_word.count(chosen_word)
    if count >=1 and chosen_word in used_words == False:
        used_words.append(chosen_word)
        i= hide_word.find(chosen_word)
        word_line[i] = chosen_word
        count -= 1
       


def hangman_game():    
    hide_word = choice(list_words)
    word_line = "_" * len(hide_word)
    while attempts >=1:
        if '_' in word_line:
            choosing_word()
        else:
            print(word_line)
            print('you did it!!! ^u^ ')
            points +=1
    if attempts == 0:
        print('no more attempts... sorry morry')


def game_over():
    print('Game Over') 
    show_points()
    print('Thanks for playing') 
    again == 0


def show_points():
    print('your score is: ' + str(points))

def gameboot():   
    while again == 1:
        show_points()
        used_words = []
        coins = int(input('Do yo want to play? Yes = 1 / No = 0: '))
        if coins == 1:
            attemps = 10
            hangman_game()
        elif coins == 0:
            game_over()
        else: 
            print('Wrong input')
 
        

        


list_words = ['memekyun', 'panochon', 'mamachona', 'papikyun', 'refresco']
points = 0
again = 1
attempts = 0
coins = 0
used_words = []

if __name__ == '__main__':
    gameboot()