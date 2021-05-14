
class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ","")


    def valid(self):
        if not self.card_num.isalnum() or len(self.card_num) <= 1:
            return False
        else:
            evens = [(int(i) * 2) - 9 if (int(i) * 2) > 9 else int(i) * 2 for i in self.card_num[-2::-2]]
            odds = [int(i) for i in self.card_num[-1::-2]]
            check_sum = sum(evens) + sum(odds)
            if check_sum % 10 == 0:
                return True
            else:
                return False
