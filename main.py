from card import *


def main():
    deck = []
    for f in CardFace:
        for v in CardValue:
            c = Card(f, v)
            deck.append(c)
            print(c)


if __name__ == "__main__":
    main()
