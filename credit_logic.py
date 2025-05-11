CREDITS = 1000

class KeepScore():
    def __init__(self):
        self.credits = CREDITS

    # Reduce credis by 100 each round
    def bet(self):
        self.credits -= 100

    # Score awards
    def payout(self, hand):
        hand_nums = sorted([int(x[:-1]) for x in hand])
        hand_kinds = [x[-1] for x in hand]

        # Track one or two pairs, three of a kind, fullhouse and four of a kind
        '''Janky thinking of a better solution'''
        start = 0
        end = 1
        end_result = ""
        while end < 5:
            count = 0
            while end < 5 and hand_nums[start] == hand_nums[end]:
                end += 1
                count += 1
            start = end
            end += 1
            if count == 1:
                end_result += "pair"
            elif count == 2:
                end_result += "three"
            elif count == 3:
                end_result += "four"
        if end_result == "pair":
            print("One pair")
            self.credits += 100
        elif end_result == "pairpair":
            print("Two pairs")
            self.credits += 200
        elif end_result == "three":
            print("Three of a kind")
            self.credits += 400
        elif end_result == "threepair" or end_result == "pairthree":
            print("Full House")
            self.credits += 1500
        elif end_result == "four":
            print("Four of a kind")
            self.credits += 3000

        # Check for straights and flushes
        if max(hand_nums) == 13 and 1 in hand_nums:
            hand_nums = hand_nums[1:] + [14]
        if hand_nums == list(range(min(hand_nums), max(hand_nums)+1)) and hand_kinds.count(hand_kinds[0]) == len(hand_kinds):
            print("Straight Flush!!")
            self.credits += 5000
        elif hand_kinds.count(hand_kinds[0]) == len(hand_kinds):
            print("Flush")
            self.credits += 800
        elif hand_nums == list(range(min(hand_nums), max(hand_nums)+1)):
            print("Straight")
            self.credits += 600

    def game_over(self):
        if self.credits <= 0:
            return True
        return False
            
    
