from deck import Deck


def main():
    new_deck = Deck()

    new_deck.first_draw()
    print(new_deck.hand)
    print(new_deck.seen)
    new_deck.card_drop()
    print(new_deck.hand)
    print(new_deck.seen)
    new_deck.clear_hand()
    print(new_deck.hand, new_deck.seen)

if __name__ == "__main__":
    main()