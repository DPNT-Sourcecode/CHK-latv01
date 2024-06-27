from collections import Counter
import re
class Specials:
    def __init__(self):
        self.items = dict()

    def add_special(self, key, value):
        self.items[key] = value

    def get_special(self, key, value):
        temp_value = value
        specials_price = 0
        if key in self.items:
            ret = []
            for v in self.items[key]:
                covered = int(temp_value) // v[0]
                if covered > 0:
                    ret.append(v[1])
                    temp_value -= covered * v[0]
                    specials_price += covered * v[1]
            return temp_value, specials_price
        else:
            return value, 0

class FreeSpecial(Specials):
    def __init__(self):
        super().__init__()

    def get_special(self, key, value):
        if key in self.items:
            ret = []
            for v in self.items[key]:
                covered = int(value) // v[0]
                if covered > 0:
                    ret.append((v[1], covered))
            return ret
        else:
            return []

class Offer:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def get_total(self, amount, specials):
        items_left, total = specials.get_special(self.item, amount)
        total += items_left * self.price

        return total

        # if self.special,"":
        #     return self.price * amount
        # else:
        #     special = self.special.split(" for ")
        #     stripped_amount = re.search(r'[0-9]+',special[0]).group()
        #
        #     if int(stripped_amount) > amount:
        #         return self.price * amount
        #
        #     not_covered = amount % int(stripped_amount)
        #     covered = amount // int(stripped_amount)
        #     return self.price * not_covered + int(special[1]) * covered

class Offers:
    def __init__(self):
        self.items = dict()

    def add_item(self, item: Offer):
        self.items[item.item] = item

    def specials(self, item):
        return self.items[item]

    def get_offer(self, item):
        try:
            return self.items[item]
        except KeyError:
            return None

# noinspection PyUnusedLocal
# skus = unicode string

specials = Specials()

specials.add_special("A", [(5, 200), (3, 130)])
specials.add_special("B", [(2, 45)])

free_specials = FreeSpecial()
free_specials.add_special("E", [(2, "B")])
free_specials.add_special("F", [(3, "F")])

offers = Offers()
offers.add_item(Offer("A", 50))
offers.add_item(Offer("B", 30))
offers.add_item(Offer("C", 20))
offers.add_item(Offer("D", 15))
offers.add_item(Offer("E", 40))
offers.add_item(Offer("F", 10))


def checkout(skus):
    if type(skus) is not str:
        return -1

    if skus != "" and re.fullmatch(r'[A-Z]+', skus) is None:
        return -1

    counted = Counter(skus)
    total = 0

    free_items = []
    for k in counted:
        fs = free_specials.get_special(k, counted[k])
        free_items += fs

    for fi, fc in free_items:
        if fi in counted and counted[fi] > 0:
            counted[fi] -= fc

    for k in counted:
        offer = offers.get_offer(k)
        if offer:
            total += offer.get_total(int(counted[k]), specials)

    return total

# print(checkout("A"), 50)
# print(checkout("B"),  30)
# print(checkout("C"),  20)
# print(checkout("D"),  15)
# print(checkout("ABCa"),  -1)
# print(checkout("-"),  -1)
# print(checkout("AxA"),  -1)
# print(checkout("ABCD"), 115)
# print(checkout("A"), 50)
# print(checkout("AA"), 100)
# print(checkout("AAA"), 130)
# print(checkout("AAAA"), 180)
# print(checkout("AAAAA"), 230)
# print(checkout("AAAAAA"), 260)
# print(checkout("B"), 30)
# print(checkout("BB"), 45)
# print(checkout("BBB"), 75)
# print(checkout("BBBB"), 90)
# print(checkout("ABCDABCD"), 215)
# print(checkout("BABDDCAC"), 215)
# print(checkout("AAABB"), 175)
# print(checkout("ABCDCBAABCABBAAA"),  505)
# print(checkout("AAAAAAAABCDEE"))
# print(checkout("EEEEBB"), 160)
# print(checkout("BEBEEE"), 160)
# print(checkout("BEBEEEFF"), 180)
# print(checkout("BEBEEEFFF"), 180)
# print(checkout("BEBEEEFFFF"), 190)
# print(checkout("BEBEEEFFFFF"), 200)
