# Kelvin DU
# 101152192
# bonus attempted

"""
    0. In main function, call play() for as long as player wants to play the game
    1. at the beginning of each round give the player a hand
    2. after giving the player a hand ask if the player wants to hit or stand
        a. if hit then deal the player another card with the dealCard function
            - deal card function will then choose a card from the deck that is passed
                as an arguement to select a random card in the deck to deal
            - deal card function will then remove the dealed card from the available deck
            - deck resets every round
        b. if stand then end round and subtract current hand from score
    3. check if hand is bust
        if not bust then calculate sum and ask the user for hit or stand repeat 2.
    4. make sure that if the hand has either j, q, or k that values are set appropriately
        a. also make sure that ace is set to 11 when sum is under 21 and 1 when sum is over 21
"""
import random


def play():
    """
    play(None) -> returns nothing, controls the mechanics of one complete
    execution of your game (not including replays)
    """
    score = 100
    deck = [x for x in range(1, 14) for _ in range(4)]
    hand = []
    for round in range(1, 6):
        sum = 0
        for card in range(2):  # gives player a hand
            newCard = dealCard(deck)
            hand.append(newCard)  # adds cards to hand
            deck.remove(newCard)
        sum = sumHand(hand)
        print("Round ", round)
        print("Score ", score)
        displayHand(hand)

        while sum <= 21:
            choice = input("Would you like to 'hit' or 'stand': ")
            if choice == 'hit':
                newCard = dealCard(deck)
                deck.remove(newCard)
                hand.append(newCard)
                sum = sumHand(hand)
                displayHand(hand)
                if sum > 21:
                    print("Bust!")
                    score = score - 21
                    break
            elif choice != 'stand':
                print("Please enter a valid choice.")
            else:
                score = score - (21 - sum)
                break
        hand = []
    print(getRank(score))


def sumHand(hand):
    """
    sumHand(list) -> int - sums and returns the value of the inputted hand
    according to the rules above
    """
    sum = 0
    for card in hand:
        # check to see if the current card is either jack, queen, king
        if 11 <= card <= 13:
            # sets the current card that is J, Q, or K to be 10
            sum += 10
        elif card == 1:
            # might need to change this to greater first than less than
            if sum > 21:
                sum += 1
            else:
                sum += 11
        else:
            sum += card
    return sum


def displayHand(hand):
    """
    displayHand(list) - returns nothing, but displays the given hand as well
    as the given hand's sum to the console
    """
    outputString = "Your hand: "
    for card in hand:
        char = ""
        if card < 11 and card != 1:
            char = str(card)
        else:
            if card == 11:
                char = 'J'
            elif card == 12:
                char = 'Q'
            elif card == 13:
                char = 'K'
            else:
                char = 'A'
        outputString += ' ' + char
    outputString += ' (' + str(sumHand(hand)) + ')'
    print(outputString)


def dealCard(deck):
    """
    dealCard() -> int - returns a random card
    """
    card = deck[random.randint(0, len(deck))]
    return card


def getRank(score):
    """
    getRank(int) -> string - returns the rank corresponding to
    the inputted total points
    """
    outputString = "Your rank : "
    if score > 95:
        outputString += "Ace!"
    elif score > 85:
        outputString += "King"
    elif score > 75:
        outputString += "Queen"
    elif score > 50:
        outputString = "Jack"
    elif score > 25:
        outputString = "Commoner"
    elif score >= -5:
        outputString = "Noob"
    return outputString


def main():
    choice = ''
    while True:
        play()
        choice = input("Do you want to play the game again? 'y', 'n' ")
        if choice == 'y':
            continue
        elif choice == 'n':
            break
        else:
            print("Please enter a valid choice. ")
            choice = input("Do you want to play the game again? 'y', 'n' ")


main()
