def example1():

    print("Please type in a number:")
    n = float(input())

    print("Please type in a number:")
    user_input = input()

    while user_input != "STOP":
        n = n + float(user_input)
        print("Please type in a number:")
        user_input = input()

    print(n)


def example2():
    print("Please type in a number:")
    user_input = input()

    if user_input == "STOP":
        return 0
    else:
        return float(user_input) + example2()


def example3(numbers):

    pairs = []

    for first_number in numbers:
        for second_number in numbers:
            if first_number + second_number == 10:
                pairs.append((first_number, second_number))

    return pairs


# You get given two cards
# You want to get as close to
# but not over 21
# KQJ are worth 10
# Ace is worth either 1 or 11
# ALl other cards are worth their value

import random

def value(hand):
    return 5

def blackjack():

    cards = ["K", "Q", "J", "A",
             2, 3, 4, 5,
             6, 7, 8, 9,]

    card_1 = random.choice(cards)
    card_2 = random.choice(cards)

    hand = [card_1, card_2]

    while True:
        print(hand)
        print(value(hand))

        if value(hand) > 21:
            # Terminate/End
            print("You've lost!")

            break
        else:
            print("Do you want another card?")
            user_input = input()

            if user_input == "y":
                new_card = random.choice(cards)
                hand.append(new_card)
            else:
                print("Ok, go home, your hand value is")
                print(value(hand))

    print("Game is over!")


blackjack()
