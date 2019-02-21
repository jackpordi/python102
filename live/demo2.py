import random

def blackjack():
    cards = ["K", "Q", "J", "A", 2, 3, 4, 5, 6, 7, 8, 9]
    hand = [random.choice(cards), random.choice(cards)]
    print(hand)


blackjack()
