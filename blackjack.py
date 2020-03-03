# Kelvin DU
# 101152192
# bonus attempted

# at the beginning of the game deal 2 cards
# calculate the value of the hand

import random


def play():
    score = 100
    deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
            8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
    hand = []
    for round in range(1, 6):
        for card in range(2):  # gives player a hand
            hand.append(dealCard(hand))
        print("Round ", round)
        print("Your hand: ", hand)
        sum = sumHand(hand)
        if sum > 21:
            print("Bust")
        elif sum == 21:
            print("BlackJack")
        hand = []


def sumHand(L):
    sum = 0
    for i in range(2):
        sum += L[i]
    return sum


def displayHand(L):
    index = 0
    while index <= len(L):
        print(L[index])
        index += 1


def dealCard(L):
    card = random.randint(1, 13)
    return card


def main():
    play()


main()
