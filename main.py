from card import *
from random import shuffle


def main():
    deck = []
    for f in CardFace:
        for v in CardValue:
            c = Card(f, v)
            deck.append(c)
            # print(c)

    shuffle(deck)

    card0 = deck.pop()
    card1 = deck.pop()

    print(card0)
    print(card1)

    hand_value = card0.point_value() + card1.point_value()
    print(f"my hand value is {hand_value}")


if __name__ == "__main__":
    main()
