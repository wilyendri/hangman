import random

def hangman(word):
    wrong = 0
    stages = ["", "________   ","|      ","|    |   ", "|    O   ","|   /|\   ",
              "|   / \   ","|      "]
    rletters = list(word)
    board = ["__"]*len(word)
    win = False
    print("Welcome to Hangman Game: Guess the hidden word and you'll win, otherwise you'd be a looser")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter "
        char = input(msg)
        if char in rletters:
            charindx = rletters.index(char)
            board[charindx] = char
            rletters[charindx] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("Congrats! You've guessed the word! You've Won!")
            print(" ".join(board))
            win= True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Buuuhhh!!! You've lost!!")
        print("The word was {}.".format(word))



while True:
    player_words1 = input("Type a word to guess ")
    player_words2 = input("Type a second word to guess ")
    player_words3 = input("Type a third words to guess ")
    player_words4 = input("Type a forth words to guess ")
    player_words5 = input("Type a fith words to guess ")
    all_words = [player_words1, player_words2, player_words3, player_words4, player_words5]
    #random_word= ["cat", "dog", "horse", "sneake", "random"]
    random_index = random.randint(0,len(all_words)-1)
    hangman(all_words[random_index])
    play_again = input("Want to play again? [Y/N] ")
    if play_again == 'N' or play_again == 'n':
        break


            
        
            
                  
            
            
            
