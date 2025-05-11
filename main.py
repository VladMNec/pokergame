from deck import Deck
from credit_logic import KeepScore


def main():
    new_deck = Deck()
    score = KeepScore()

    # new_deck.first_draw()
    # print(new_deck.hand)
    # new_deck.card_drop()
    # print(new_deck.hand)
    score.payout([1, 2, 3, 4, 1])
    new_deck.clear_hand()


if __name__ == "__main__":
    main()