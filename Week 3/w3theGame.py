# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 08:49:54 2018

@author: simpp
"""
secretWord = "kissa"
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    ''' 
    guesses = 8
    lettersGuessed = []
    mistakesMade = 0
    win = False
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
     
    while mistakesMade < 8 and win == False:
        print("-------------")
        print("You have " + str(guesses) + " guesses left")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        roughGuess = input("Please guess a letter: ")
        guess = roughGuess.lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guess)
            if guess in secretWord:
                guessedWord = getGuessedWord(secretWord, lettersGuessed)
                print("Good guess: " + guessedWord)
                if guessedWord == secretWord:
                    print("-------------")
                    print("Congratulations, you won!")
                    win = True            
            else:
                guesses -= 1
                mistakesMade += 1
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
    if win == False:
        print("-------------")
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")