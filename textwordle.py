from colorama import Fore
from word_generator import *
import requests
import sys

def get_word(length):
    """Generates a random 5-letter word for Wordle"""

    def get(url, headers="", params=""):
        """ GET and return an API response given the following
            url (string)
            headers (dict with key(string),value(string) pairs)
            params (dict with key(string),value(string) pairs)
        """
        return requests.request("GET", url, headers=headers, params=querystring)

    if __name__ == "__main__":
        # setup options for GET request
        url = "https://random-words5.p.rapidapi.com/getRandom"
        querystring = {"wordLength":length}
        headers = {
                    "X-RapidAPI-Key": "93b7bd7839msh0049868b4aa1aaap132838jsn5c44e68abeba",
                    "X-RapidAPI-Host": "random-words5.p.rapidapi.com"
        }

        # send GET request (use helper function)
        word = get(url, headers, querystring)
        
        # if response status code is successful
        if word.status_code == 200:
            return word.text
                
        # else error getting response (print status code)
        else:
            print("Error getting response, status code recieved was " + str(word.status_code))
            sys.exit()

class Square:
    """Corresponds to one square (of five) in each row of Wordle. Stores information about
    the correct letter and changes color to represent whether the given letter is correct,
    misplaced, or not in the word."""
    
    def __init__(self, position, correct_letter, input_letter="", board=None, status="incorrect"):
        """Initializes a Wordle letter square with the given letter, correct letter, 
        position, and board.
        
        Parameters
        ----------
        position : int
            The column of the square (an integer between 0 and 4), corresponding to the index
            of the letter in the word
        correct_letter : str
            The correct letter corresponding to the word at that position
        input_letter : str
            The letter given by the player corresponding to the letter's position
        board : Board
            The game board to which this letter belongs
        """
        self._position = position
        self._correct_letter = correct_letter
        self._input_letter = input_letter
        self._board = board
        self._status = status

    def get_input(self):
        """Returns the player-inputted letter"""
        return self._input_letter

    def set_input(self, letter):
        """Takes the player-inputted letter and changes the square's input_letter from an empty string"""
        self._input_letter = letter

    def get_correct_letter(self):
        """Returns the correct letter"""
        return self._correct_letter

    def get_status(self):
        return self._status

    def set_status(self, status):
        if status in ["incorrect", "misplaced", "correct"]:
            self._status = status

    def __str__(square):
        """A string representation of each letter on the terminal output"""
        colors = {'incorrect': Fore.WHITE, 'misplaced': Fore.YELLOW, 'correct': Fore.GREEN}
        return colors[square.get_status()] + square.get_input()

class Board:
    """A 6x5 board of Letter objects"""

    def __init__(self, word):
        """Initializes a new wordle Board.
        
        Parameters
        ----------
        word : str
            A 5-letter word that is the solution to the game.
        """
        
        self._word = word

        self._square_grid = []
        for i in range(6):
            row = []
            for j in range(5):
                square = Square(j, word[j], input_letter="")
                row.append(square)
            self._square_grid.append(row)

        # a list of words (str) that have been guessed
        self._guesses = []
        # iterate over guesses
        for i in range(len(self._guesses)):
            # iterate over letters in each guess (5-letter words)
            for j in range(5):
                guess_letter = self._guesses[i][j]
                square = self._square_grid[i][j]
                square.set_input(guess_letter)
                if square.get_input() == square.get_correct_letter():
                    square.set_status("correct")
                elif square.get_input() in word:
                    square.set_status("misplaced")


    def get_square(self, row, col):
        """Returns the Square at the specified row and column"""

        return self._square_grid[row][col]

    def update_squares(self):
        # iterate over guesses
        for i in range(len(self._guesses)):
            # iterate over letters in each guess (5-letter words)
            for j in range(5):
                guess_letter = self._guesses[i][j]
                square = self._square_grid[i][j]
                square.set_input(guess_letter)
                if square.get_input() == square.get_correct_letter():
                    square.set_status("correct")
                elif square.get_input() in self._word:
                    square.set_status("misplaced")

def display_board(board, guesses):
    """A string representation of the Wordle Board"""
    row_squares = []
    for row in range(len(guesses)):
        letter = [str(board.get_square(row, col)) for col in range(5)]
        row_squares.append(' '.join(letter))
    print('\n'.join(row_squares))

def game_won(guesses, correct_word):
    """Checks if the player has guessed the correct word"""
    if len(guesses) > 0 and guesses[-1] == correct_word:
        return True
    return False


# GAME LOOP
def text_wordle():
    print("Let's play Wordle on the terminal!")
    random_word = get_word(5)
    board = Board(random_word)
    attempts = 0

    while attempts < 6 and not game_won(board._guesses, board._word):
        
        guess = str(input("\nYour guess: "))
        board._guesses.append(guess)
        board.update_squares()
        print(board._guesses)
        display_board(board, board._guesses)
        attempts += 1 

    print('Game over!')


if __name__ == "__main__":
    text_wordle()
