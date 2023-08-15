# Wordle with Custom Word Lengths
By Serah Park

## Description
*Length-based Wordle:*
For my final CS10 Project, I wanted to create a game similar to Wordle, a popular game in which players try to guess a random word (updated daily) in a limited number of guesses. Once a player has made guesses, the Wordle display indicates guessed letters that are in the correct location, in the word but in the incorrect location, and not in the word. However, Wordle only uses five-letter words, so I wanted to make my own version of Wordle in which the player can choose their desired word length. I used the Random Words API from RapidAPI, which can be found [here](https://rapidapi.com/sheharyar566/api/random-words5).

*Improved Wordle:*
I wanted to modify my custom-length Wordle game to fit the color scheme of the original Wordle game, where letters in green represent correct letters in correct locations while letters in yellow represent correct letters in incorrect positions. `textwordle.py` utilizes object-oriented programming and, rather than using the Random Words API to generate words at custom lengths, the API is now used to generate a random five-letter word (like the original game).

## Dependencies
```
import requests
import sys
```

## How To Play
### Length-based Wordle
To run the script, download the lengthwordle.py file and type ```python3 lengthwordle.py``` in the command line. The terminal output will display instructions on how to play, as shown below:
```
Command Line Wordle
This game is similar to Wordle, in which you guess a randomly 
generated word with a provided length. Unlike Wordle, which uses 
five-letter words with six guesses, you can play this game with 
words of n length and n+1 guesses.
To play, type your desired word length:
```
Players will have to provide a word length greater than 2 and the terminal will prompt the player to guess words of that length. Each time a guess is made, the output will categorize the letters guessed and any letters that were matched correctly and also indicate the number of guesses remaining. For instance (the word is `apple`):
```
Your guess: adieu
Attempts remaining: 5
Correct letters, wrong spot: e
Not in word: d i u
a _ _ _ _
```
The game ends when the player correctly guesses the word in the given number of guesses, or when the player runs out of guesses.

### Improved Wordle
To run the script, download the textwordle.py file and type ```python3 textwordle.py``` in the command line. The terminal will prompt the player to provide a 5-letter guess. Each time a guess is made, the board output will be updated with the appropriate coloring of each letter as well as the number of attempts left. For instance (the word is `shiny`):
```
Your guess: gybes
You have 1 attempts remaining
w a l t z
q u i c k
n y m p h
f j o r d
g y b e s
```
The game ends when the player correctly guesses the word in the given number of guesses, or when the player runs out of guesses.
