import random
FACE_CARD_VALUE = 10
ACE_VALUE = 1
CARD_LABELS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
BLACKJACK = 21
DEALER_THRESHOLD = 16
CHOICES= ("s","h")


def main():
    """Runs a program for playing Blackjack with one player
    and a dealer
    """
    play_blackjack()

def play_blackjack():
    print("Let's Play Blackjack!\n")
    play_again="Y"
    while play_again=="Y":
        n_p_total = deal_cards_to_player()
        if n_p_total <= BLACKJACK:
            n_d_total=deal_cards_to_dealer()
            determine_outcome(n_p_total,n_d_total)
        else:
            determine_outcome(n_p_total)
        play_again=input("Play again (Y/N)?\n")
        while play_again!="Y" and play_again!="N":
            play_again=input("Play again (Y/N)?\n")
    print("Goodbye.")

def deal_card():
    """Evaluates to a character representing one of 13
    cards in the CARD_LABELS tuple
    :return: a single- or double-character string representing a playing card
    """
    card=random.choice(CARD_LABELS)
    return card

def get_card_value(card):
    """Evaluates to the integer value associated with
    the card label (a single- or double-character string)
    :param card_label: a single- or double-character string representing a card
    :return: an int representing the card's value
    """
    if card=="A":
        value=1
    elif card == "J":
        value = 11
    elif card == "Q":
        value = 12
    elif card == "K":
        value = 13
    else:
        value = int(card)
    return value

def deal_cards_to_player():
    """Deals cards to the player and returns the card
    total
    :return: the total value of the cards dealt
    """
    card_one=deal_card()
    card_two=deal_card()
    card_value_one=get_card_value(card_one)
    card_value_two=get_card_value(card_two)
    player_total=card_value_one+card_value_two
    print("Player drew",card_one,"and",card_two+".")
    print("Player's total is",str(player_total)+".","\n")
    if player_total <= BLACKJACK:
        n_p_total=player_total
        choice_p = input("Hit (h) or Stay (s)?")
        print("")
        while choice_p != "h" and choice_p != "s":
            choice_p = input("Hit (h) or Stay (s)?")
            print("")
        while choice_p == "h":
            card_p = deal_card()
            print("Player drew",str(card_p)+".")
            card_p_value=get_card_value(card_p)
            n_p_total=card_p_value+n_p_total
            print("Player's total is",str(n_p_total)+".\n")
            if n_p_total<BLACKJACK:
                choice_p= input("Hit (h) or Stay (s)?")
                print("")
            elif n_p_total==BLACKJACK:
                return n_p_total
            else:
                return n_p_total
        return n_p_total
    else:
        return player_total

def deal_cards_to_dealer():
    """Deals cards to the dealer and returns the card
    total
    :return: the total value of the cards dealt
    """
    card_one=deal_card()
    card_two=deal_card()
    card_value_one=get_card_value(card_one)
    card_value_two=get_card_value(card_two)
    dealer_total=card_value_one+card_value_two
    print("The dealer has",card_one,"and",card_two+".")
    print("Dealer's total is",str(dealer_total)+".\n")
    n_d_total=dealer_total
    if dealer_total<DEALER_THRESHOLD:
        choice_d="h"
        while choice_d=="h":
            card_d = deal_card()
            print("Dealer drew",str(card_d)+".")
            card_d_value=get_card_value(card_d)
            n_d_total=card_d_value+n_d_total
            print("Dealer's total is",str(n_d_total)+".\n")
            if n_d_total>DEALER_THRESHOLD:
                return n_d_total
            else:
                choice_d="h"
        return n_d_total
    else:
        return n_d_total

def determine_outcome(player_total, dealer_total=21):
    """Determines the outcome of the game based on the value of
    the cards received by the player and dealer. Outputs a
    message indicating whether the player wins or loses.
    :param player_total: total value of cards drawn by player
    :param dealer_total: total value of cards drawn by dealer
    :return: None
    """
    if player_total>dealer_total:
        if player_total<=BLACKJACK:
            print("YOU WIN!","\n")
        else:
            print("YOU LOSE!","\n")
    elif dealer_total>player_total:
        if dealer_total<=BLACKJACK:
            print("YOU LOSE!","\n")
        else:
            print("YOU WIN!","\n")
    elif dealer_total==player_total:
        print("YOU LOSE!","\n")


if __name__ == "__main__":
    main()

