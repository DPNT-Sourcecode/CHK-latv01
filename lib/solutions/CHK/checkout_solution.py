from collections import Counter
import re
class Offer:
    def __init__(self, item, price, special):
        self.item = item
        self.price = price
        self.special = special

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

offers = Offers()
offers.add_item(Offer("A", 50, "3A for 130"))
offers.add_item(Offer("B", 30, "2B for 45"))
offers.add_item(Offer("C", 20, ""))
offers.add_item(Offer("D", 15, ""))


def checkout(skus):
    if type(skus) is not str:
        return -1

    if skus != "" and re.fullmatch(r'[A-Z]+', skus) is None:
        return -1

    counted = Counter(skus)
    total = 0
    for k in counted:
        offer = offers.get_offer(k)
        if offer:
            total += offer.get_total(int(counted[k]))

    return total


