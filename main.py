from deck import Deck
from credit_logic import KeepScore
from tabulate import tabulate


def main():
    new_deck = Deck()
    score = KeepScore()
    print("Welcome to the janky poker game")
    print(f"Game starts with {score.credits}")
    game_on = True
    while not score.game_over() and game_on:
        print("Betting is 100 credits.")
        score.bet()
        new_deck.first_draw()
        print("Your cards")
        table = [["", "", "", "", ""], [new_deck.hand[0], new_deck.hand[1], new_deck.hand[2], new_deck.hand[3], new_deck.hand[4]], ["", "", "", "", ""]]
        print(tabulate(table, tablefmt="simple_outline"))
        new_deck.card_drop()
        table = [["", "", "", "", ""], [new_deck.hand[0], new_deck.hand[1], new_deck.hand[2], new_deck.hand[3], new_deck.hand[4]], ["", "", "", "", ""]]
        print(tabulate(table, tablefmt="simple_outline"))
        score.payout(new_deck.hand)
        new_deck.clear_hand()
        print(f"Current Credits: {score.credits}")
        continue_game = input("Play another hand?(y/n): ")
        if continue_game == "n":
            game_on = False


if __name__ == "__main__":
    main()