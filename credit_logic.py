CREDITS = 1000

class KeepScore():
    def __init__(self):
        self.credits = CREDITS

    def bet(self):
        self.credits -= 10

    def payout(self, hand):
        # hand_nums = sorted([int(x[:-1]) for x in hand])
        hand_nums = sorted([x for x in hand])
        start = 0
        end = 1
        end_count = ""
        while end < 5:
            count = 0
            while end < 5 and hand_nums[start] == hand_nums[end]:
                end += 1
                count += 1
            start = end
            end += 1
            if count == 1:
                end_count += "pair"
            elif count == 2:
                end_count += "three"
            elif count == 3:
                end_count += "four"
        if end_count == "pair":
            print("One pair")
        if end_count == "pairpair":
            print("Two pairs")
        if end_count == "three":
            print("Three of a kind")
        if end_count == "threepair" or end_count == "pairthree":
            print("Full House")
        if end_count == "four":
            print("Four of a kind")
            
            

        print(hand_nums)
    
