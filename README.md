# Wordle with Custom Word Lengths
By Serah Park

## Description
I wanted to create a game similar to Wordle, a popular game in which players try to guess a random word (updated daily) in a limited number of guesses. Once a player has made guesses, the Wordle display indicates guessed letters that are in the correct location, in the word but in the incorrect location, and not in the word. However, Wordle only uses five-letter words, so I wanted to make my own version of Wordle in which the player can choose their desired word length. I used the Random Words API from RapidAPI, which can be found [here](https://rapidapi.com/sheharyar566/api/random-words5).

## Dependencies
```
import requests
import sys
```

## How To Play
To run the script, download the wordle.py file and type ```python3 wordle.py``` in the command line. The terminal output will display instructions on how to play, as shown below:
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
