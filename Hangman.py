def hangeman_open_page():

    """This function print the open page of Hangman with the maximum tries user can do."""
    
    HANGMAN_ASCII_ART = """ 
     _    _                              
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/ """
                     
                     
    MAX_TRIES = 6                     

    print(HANGMAN_ASCII_ART, MAX_TRIES, sep="\n")
    
HANGMAN_PHOTOS = {1: "x-------x", 2: "x--------x\n|\n|\n|\n|\n|", 3: "x-------x\n|\t|\n|\t0\n|\n|\n|", 4: "x-------x\n|\t|\n|\t0\n|\t|\n|\n|", 5: "x-------x\n|\t|\n|\t0\n|      /|\\\n|\n|", 6: "x-------x\n|\t|\n|\t0\n|      /|\\\n|      /\n|", 7: "x-------x\n|\t|\n|\t0\n|      /|\\\n|      / \\\n|"}
    
file_path = input("Please enter the path of your words file: ")
index = int(input("Enter random number: "))


def choose_word(file_path, index):

    """This function choose a word from a list of words in file that the user insert.
       The specific word choose by the index.
       
       :param file_path: the path of user file
       :type file_path: _io.TextIOWrapper
       :param index: location of the word in the file
       :type index: int
       :return: secret word
       :rtype: str
       """
       
    words_file = open(file_path, 'r')  
    original_list = words_file.read().split(" ")
    
    index = index - 1
    while index >= len(original_list):
        index = index - len(original_list)
    
    secret_word = original_list[index]
    return secret_word



def print_hangman(num_of_tries):

    """This function print the status of the user Hangman by his number of tries.
    
    :param num_of_tries: number of user tries
    :type num_of_tries: int
    :return: None
    :rtype: None."""

    for key in HANGMAN_PHOTOS.keys():
        if num_of_tries == key:
            print(HANGMAN_PHOTOS[key])



def hidden_word(secret_word):

    """This function presents the secret word of the game in empty chars.
    
    :param secret_word: the secret word that choosed from the file
    :type secret_word: str
    :return: empty_secret_word
    :rtype: str"""
    
    number_of_chars = len(secret_word)
    empty_secret_word = number_of_chars * "_ "
    print(empty_secret_word)



def guess_a_letter():

    """This function asking from user for guessing a letter.
    
    :param: None
    :return: letter_guessed in lowercase
    :rtype: str"""
    
    letter_guessed = input("Please enter your letter: ")
    return letter_guessed.lower()



def check_valid_input(letter_guessed, old_letters_guessed):

    """This function checks if the letter that the user entered is valid for the game.
    
    :param letter_guessed: user guessing
    :type letter_guessed: str
    :param old_letters_guessed: list of old letters that guessed by the user
    :type old_letters_guessed: list
    :return: True if the letter is valid or False is the letter is not valid
    :rtype: bool
    """

    if (letter_guessed.isalpha() == True) and (len(letter_guessed) == 1) and (letter_guessed.lower() not in old_letters_guessed):
        return True
    else:
        return False



def try_update_letter_guessed(letter_guessed, old_letters_guessed):

    """This function updates the list of old_letters_guessed if the letter that user guessed is not in it,
       or prints an error message if user try to guess letter the in the list of old_letters_guessed.
       
    :param letter_guessed: user guessing
    :type letter_guessed: str
    :param old_letters_guessed: list of old letters that guessed by the user 
    :type old_letters_guessed: list
    :return: True if the letter not in old_letters_guessed or False if the letter in old_letters_guessed
    :rtype: bool"""
     
    if check_valid_input(letter_guessed, old_letters_guessed) == True:
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        remember_old_letters = sorted(old_letters_guessed)
        print("X\n", " -> ".join(remember_old_letters))
        return False



def letter_in_secret_word(letter_guessed, secret_word):

    """This function checks if the letter is in or not in the secret word.
    
    :param letter_guessed: user guessing
    :type letter_guessed: str
    :param secret_word: the secret word that choosed from the file
    :type secret_word: str
    :return: True if letter_guessed in the secret_word or False if not
    :rtype: bool"""
    
    if letter_guessed in secret_word:
        return True
    else:
        print(":(")
        return False



def show_hidden_word(secret_word, old_letters_guessed):

    """This function presents the secret word till now,
       the output is combination of correct letters from the old_letters_guessed and blank spaces that not guessed.
       
    :param secret_word: the secret word that choosed from the file
    :type secret_word: str
    :param old_letters_guessed: the secret word that choosed from the file
    :type old_letters_guessed: list
    :return: status of secret_word_now
    :rtype: str"""
    
    secret_word_now = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            secret_word_now += letter
        else:
            secret_word_now += "_"          
    secret_word_now =  " ".join(secret_word_now)
    return secret_word_now

  
        
def check_win(secret_word, old_letters_guessed):

    """This function checks if the user win the game or lose.
    
    :param secret_word: the secret word that choosed from the file
    :type secret_word: str
    :param old_letters_guessed: the secret word that choosed from the file
    :type old_letters_guessed: list
    :return: True if the user win of False if the user lose
    :rtype: bool"""
    
    win = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            win += '$'
            
    if len(win) == len(secret_word):
        return True
    else:
        return False




def main():

    hangeman_open_page()
    print("\n")
    print("Let's start!\n")
    
    wrong_guess = 0
    num_of_tries = 1
    
    old_letters_guessed = list()
    secret_word = choose_word(file_path, index)
    print_hangman(num_of_tries)
    hidden_word(secret_word)
    
    while wrong_guess in range(6):
        letter_guessed = guess_a_letter()
        if try_update_letter_guessed(letter_guessed, old_letters_guessed) == True:
            if letter_in_secret_word(letter_guessed, secret_word) == False:
                wrong_guess += 1
                num_of_tries += 1
                print("\n")
                print_hangman(num_of_tries)
                print("\n")
                print(show_hidden_word(secret_word, old_letters_guessed))
            else:
                print(show_hidden_word(secret_word, old_letters_guessed))
                if check_win(secret_word, old_letters_guessed) == True:
                    print("WIN")
                    break
                    
    if wrong_guess == 6:
        if check_win(secret_word, old_letters_guessed) == True:
            print("WIN")  
        else:
            print("LOSE")



            
if __name__ == "__main__":
    main() 