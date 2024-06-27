from collections import Counter
import re
class Specials:
    def __init__(self):
        self.items = dict()

    def add_special(self, key, value):
        self.items[key] = value

    def get_special(self, key, value):
        if key in self.items:
            return self.items[key]
        else:
            return None

class FreeSpecial(Specials):
    def __init__(self):
        super().__init__()

class Offer:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def get_total(self, amount):
        if self.special == "":
            return self.price * amount
        else:
            special = self.special.split(" for ")
            stripped_amount = re.search(r'[0-9]+',special[0]).group()

            if int(stripped_amount) > amount:
                return self.price * amount

            not_covered = amount % int(stripped_amount)
            covered = amount // int(stripped_amount)
            return self.price * not_covered + int(special[1]) * covered

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

offers = Offers()
offers.add_item(Offer("A", 50))
offers.add_item(Offer("B", 30))
offers.add_item(Offer("C", 20))
offers.add_item(Offer("D", 15))
offers.add_item(Offer("E", 40))


def checkout(skus):
    if type(skus) is not str:
        return -1

    if skus != "" and re.fullmatch(r'[A-Z]+', skus) is None:
        return -1

    counted = Counter(skus)
    total = 0

    for k in counted:
        fs = free_specials.get_special(k, counted[k])
        print(fs)

    for k in counted:
        offer = offers.get_offer(k)
        if offer:
            total += offer.get_total(int(counted[k]))

    return total


checkout("AAAAAAAABCDEE")



