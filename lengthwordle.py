import requests
import sys

def main():
    print("Command Line Wordle\nThis game is similar to Wordle, in which you guess a randomly \ngenerated word with a provided length. Unlike Wordle, which uses \nfive-letter words with six guesses, you can play this game with \nwords of n length and n+1 guesses.")
    length = int(input("To play, type your desired word length: "))

    def get(url, headers="", params=""):
        """ GET and return an API response given the following
            url (string)
            headers (dict with key(string),value(string) pairs)
            params (dict with key(string),value(string) pairs)
        """
        return  requests.request("GET", url, headers=headers, params=querystring)

    if __name__ == "__main__":
        # if correct argument given (a number indicating the word length is given)
        if length > 2 and type(length) == int:
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

                # print entry for randomly generated word
                secret_word = word.text
                
            # else error getting response (print status code)
            else:
                print("Error getting response, status code recieved was " + str(word.status_code))

        else:
            print("Please try again with a word length greater than 2.")
            sys.exit()

    print("You have " + str(len(secret_word) + 1) + " guess attempts.")
    attempts = 0
        
    while(True):

        # set up game format/variables & sets to store letters
        blanks = ['_'] * len(secret_word)
        not_in_word = set()
        in_word = set()   
        max_attempts = len(secret_word)

        # allows user to guess until they use up all guesses
        while attempts <= max_attempts:

            guess = str(input("\nYour guess: "))
            attempts +=1
            print("Attempts remaining: " + str(max_attempts - attempts + 1))
            
            # if user guesses the word correctly
            if guess == secret_word:
                print("Congratulations! The word was " + secret_word + " and you have guessed the word after " + str(attempts) + " attempts.")
                break;
                
            else:
                # modifies blanks & sets with guessed letters
                for i in range(len(secret_word)):
                    if len(guess) != len(secret_word):
                        print("Please enter a word that is " + str(len(secret_word)) + " letters long.")
                        break;
                    if secret_word.split().count(guess[i]) > 1:
                        in_word.add(guess[i])
                        blanks[i] = secret_word[i]
                    elif guess[i] == secret_word[i]:
                        blanks[i] = secret_word[i]
                    elif guess[i] in secret_word:
                        in_word.add(guess[i])
                    elif guess[i] not in secret_word:
                        not_in_word.add(guess[i])

                print("Correct letters, wrong spot: " + ' '.join(in_word))
                print("Not in word: " + ' '.join(not_in_word)) 
                print(' '.join(blanks))

            # terminates game if user does not guess in max attempts
            if attempts > max_attempts:
                print("\nYou have run out of guesses. The word was " + secret_word + ".")
        break;
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
