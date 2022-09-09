import random
play = True
HANGMAN_PICS = ['''
   +---+ 
       |
       |
       |
       |
      ===''','''
   +---+
   O   |
       |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
       |
      ===''']
def hangman_picture():
    if lives == 6:
        print(HANGMAN_PICS[0])
    elif lives == 5:
        print(HANGMAN_PICS[1])
    elif lives == 4:
        print(HANGMAN_PICS[2])
    elif lives == 3:
        print(HANGMAN_PICS[3])
    elif lives == 2:
        print(HANGMAN_PICS[4])
    elif lives == 1:
        print(HANGMAN_PICS[5])
    elif lives == 0:
        print(HANGMAN_PICS[6])
    return

welcome_message = """
    
    
            Welcome to HANGMAN :)                       
    Version "Guess a capital of a country"
    All you need to do is guess a capital city 
    of a randomly selected country.       
    
    We have 3 difficulty levels.        
    Level 1 - is the easiest
    Level 2 - is middle level       +---+
    Level 3 - is the hardest        O   |
                                   /|\  |
    Good luck and have fun :)       |   |         
                                   / \  |
                                        |
                                   ========
     ***************************************************
    
    """ # we can adjust it to whatever 
print(welcome_message)
user_name = input('Enter your name, to play the game: ').capitalize()

while play:
    
    
    lives_required_for_hint = 0
    while lives_required_for_hint == 0:

        level_choice = int(input("Please choose level from 1-3: "))
        
        print('\nHello ' + user_name + ', try to guess the capital city, randomly chosen for you.\n' )
        
        if level_choice == 1:
            lives_required_for_hint = 7
        elif level_choice == 2:
            lives_required_for_hint = 3
        elif level_choice == 3:
            lives_required_for_hint = 1
        else:
            print("Wrong level chosen")
            
    
    # preparation
    f = open('countries-and-capitals.txt')
    lines = f.readlines()
    f.close
    country_capital = random.choice(lines)
    words = country_capital.strip().split(' | ') #.strip removes unnecessarily space, .split splits the string at the specified separator, and returns a list

    # print(country_capital)
    country = words[0].upper()
    print("**********************************************")
    print(f"this won't be shown in game mode:{country}")
    capital = words[1].upper() #word in capital part of file 
    print(f"this won't be shown in game mode:{capital}")
    print("**********************************************")

    tiles = []
    missed_letters = []
    hit_letters = []
    is_winner = False
    
    # levels 1-3
    lives = 7 
    for letter in capital:                  #letter - litera w wyrazie
        if(letter == " "):
            tiles.append(" ")
        else:
            tiles.append("_")

    while lives > 0 and not is_winner:
        print(" ".join(tiles))  # glue letters from tiles array with space 
        print('')
        
        if lives <= lives_required_for_hint: # we can amend that in lower levels to appear quicker 
            print('\nHint: the capital of ' + words[0] + "\n")  # gives a hint
            
        print("Lives: " + str(lives)) 
        print("Missed letters: "+", ".join(set(missed_letters))) # set doesn't allow duplicates
        print("Hit letters: "+", ".join(set(hit_letters)))
        guess = input('Enter a letter or full word: ').upper()
         
        letter_occurrences = 0
        if len(guess) > 1:  # for whole word
            if guess == capital:
                is_winner = True
            else:
                print('Wrong answer!')
                lives -= 1
        else:   # for the single letter, adding letters to tiles
            index_letter = 0                            #index_letter - wystepowanie danej litery, letters in tile list 
            for letter in capital: # loop goes through every letter in capital 
                if letter == guess:
                    if index_letter > 0: # if its not the first letter
                        tiles[index_letter] = letter.lower() #  Change all the letters after first letter in tiles to lower case 
                    else:
                        tiles[index_letter] = letter
                    letter_occurrences += 1  # occurency in word (capital)
                    if letter not in hit_letters: # if this letter isn't already in hit_letters add it there
                        hit_letters.append(guess)
                elif guess in missed_letters: # missed letter is repeated again
                    letter_occurrences += 1                  
                index_letter += 1  
            
            current_guess = "".join(tiles)
            print(current_guess)

            if  current_guess.upper() == capital:  
                is_winner = True
            if letter_occurrences == 0:
                missed_letters.append(guess)
                lives -= 1
                print('\n Wrong letter!\n')
                print('')
            
        hangman_picture()        
    if lives == 0:
        print('Game over! :(')

    if is_winner:
        print(f"You won! :) Congratulations {user_name} the capital city of {country.capitalize()} is: {capital.capitalize()}\n")
        f.close()
    replay_game = input('\n Type quit to exit. Press enter to play again. \n')
    if replay_game == "quit":
        print("Thank you for playing and good-bye")
        play = False

