import random

NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
KIND = ["S", "C", "H", "D"]

class Deck:
    def __init__(self):
        self.deck = []
        self.seen = set()
        self.hand = []
        for k in KIND:
            for n in NUMBERS:
                card = f"{n}" + k
                self.deck.append(card)

    def draw_card(self):
        new_card = random.randint(0, 51)
        return self.deck[new_card]

    def first_draw(self):
        while len(self.hand) < 5:
            new_card = self.draw_card()
            if new_card not in self.seen:
                self.seen.add(new_card)
                self.hand.append(new_card)
    
    def second_draw(self, change=list()):
        if len(change) > 0:
            change.sort()
            new_hand = []
            for n in change:
                if n > 4 or n < 0:
                    print(f"{n} not a valid card number")
                    self.card_drop()
            for i in range(0, 5):
                if i not in change:
                    new_hand.append(self.hand[i])
            self.hand = new_hand


    def card_drop(self):
        drop = input("Choose cards to drop (0-4), with space between each number").split(" ")
        drop = list(map(int, drop))
        self.second_draw(change=drop)