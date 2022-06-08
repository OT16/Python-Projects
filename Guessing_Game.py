import random
import sys
MAX_MISSES = 5
BORDER_LENGTH = 30
SINGLE_CHAR_LENGTH = 1

def display_game_state(chars, misses):
    """
    Displays the current state of the game: the list of characters to display
    and the list of misses.
    """
    print()
    print('=' * BORDER_LENGTH)
    print()
    print("Word:\t{}\n".format(space_chars(chars)))
    print("Misses:\t{}\n".format("".join(misses)))

def main():
    filepath = sys.argv[-1]
    run_guessing_game(filepath)

def blank_chars(word):
    """Returns a list of underscore characters with the same length as word.
    :param word: target word as a string
    :return: a list of underscore characters ('_')
    """
    list=[]
    for i in range(len(word)):
        list+="_"
    return list

def space_chars(chars):
    """Returns a string with the characters in chars list separated by spaces.
    :param chars: a list of characters
    :return: a string containing characters in chars with intervening spaces
    """
    str_one=("")
    count=len(chars)
    for i in range(count):
        x=chars[i]
        str_one=str_one+x+" "
    str_one=str_one[:-1]
    return str_one

def get_guess():
    """Prompts the user for a guess to check for the game's current word. When the user
    enters input other than a single character, the function prompts the user again
    for a guess. Only when the user enters a single character will the prompt for
    a guess stop being displayed. The function returns the single-character guess
    entered by the user.
    :return guess: a single character guessed by user
    """
    guess="AB&"
    while guess!=guess.isalpha() or len(guess)!=1:
        if len(guess)==1 and guess.isalpha():
            return guess.lower()
        else:
            guess=input("Guess:\t")

def check_guess(word, guess):
    """Returns a list of positions where guess is present in word.
    An empty list should be returned when guess is not a single
    character or when guess is not present in word.
    :param word: target word as a string
    :param guess: a single character guessed by user
    :return positions: list of integer positions
    """
    list_one=[]
    for i in range(len(word)):
        if word[i]==guess:
            list_one.append(i)
    return list_one

def update_chars(chars, guess, positions):
    """Updates the list of characters, chars, so that the characters
    at the index values in the positions list are updated to the
    character guess.
    """
    for i in positions:
        chars[i]=guess

def add_to_misses(misses, guess):
    """Adds the character guess to the misses list.
    """
    misses.append(guess)

def update_state(chars, misses, guess, positions):
    """Updates the state of the game based on user's guess. Calls the function update_chars() when
    the positions list is not empty to reveal the indices where the character guess is present. Calls the
    function add_to_misses() when the positions list is empty to add guess to the misses list.
    """
    if len(positions)!=0:
        update_chars(chars,guess,positions)
    else:
        add_to_misses(misses,guess)

def is_round_complete(chars, misses):
    """Indicates whether or not a round has ended. This function returns True
    when the user has successfully guessed the target word or exceeds the
    number of allowed misses. Otherwise, the function returns False,
    indicating that the round is not complete. A message revealing the
    user's success or failure guessing the target word is output by this
    function when the round is complete.
    :param chars: a list of characters
    :param misses: list of guesses not present in target word
    :return status: True when round is finished, False otherwise
    """
    len_of_char=len(chars)
    z=0
    for i in chars:
        if i!="_":
            z+=1
    if z==len_of_char:
        print("")
        print("YOU GOT IT!")
        return True
    elif len(misses)>MAX_MISSES:
        print("")
        print("SORRY! NO GUESSES LEFT.")
        return True
    else:
        return False

def read_words(filepath):
    """Opens a file of word located at filepath, reads the file of words line by line,
    and adds each word from the file to a list. The list is returned by the
    function
    :param filepath: path to input file of words (one per line)
    :return word_list: list of strings contained in input file
    """
    word_list=[]
    word_string=("")
    file_name=open(filepath,"r")
    wlist=file_name.readlines()
    for strings in range(len(wlist)):
        for word in wlist[strings]:
            if word=="\n":
                word_list.append(word_string)
                word_string=("")
            else:
                word_string+=word
    word_list.append(word_string)
    file_name.close()
    return word_list

def get_word(words):
    """Selects a single word randomly from words list and returns it.
    :param words: list of strings
    :return word: string from words list
    """
    x=random.randrange(len(words))
    word=words[x]
    return word

def is_game_complete():
    """Prompts the user with "Play again (Y/N)?". The question is repeated
    until the user enters a valid response (one of Y/y/N/n). The function
    returns False if the user enters 'Y' or 'y' and returns True if the user
    enters 'N' or 'n'.
    :return response: boolean representing game completion status
    """
    play_again=None
    while play_again!="Y" and play_again!="y" and play_again!="N" and play_again!="n":
        play_again=input("Play again (Y/N)? ")
    if play_again=="Y" or play_again=="y":
        return False
    else:
        return True

def run_guessing_game(words_filepath):
    """Controls running The Guessing Game. This includes parsing
    the words file and executing multiple rounds of the game.
    :param words_filepath: the location of the file of words for the game
    :return: None
    """
    try:
        words=read_words(words_filepath)
        print("Welcome to The Guessing Game!")
        game=False
        while game!=True:
            complete=False
            misses=[]
            word=get_word(words)
            chars=blank_chars(word)
            while complete!=True:
                display_game_state(chars, misses)
                guess=get_guess()
                position=check_guess(word,guess)
                update_state(chars,misses, guess, position)
                complete=is_round_complete(chars,misses)
            display_game_state(word,misses)
            game=is_game_complete()
        print("\nGoodbye.")
    except FileNotFoundError:
        print("The provided file location is not valid. Please enter a valid path to a file.")


if __name__ == '__main__':
    main()
