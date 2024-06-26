from Collections import Counter

class Offer:
    def __init__(self, item, price, special):
        self.item = item
        self.price = price
        self.special = special


class Offers:
    def __init__(self):
        self.items = dict()

    def add_item(self, item: Offer):
        self.items[item.item] = item

    def specials(self, item):
        return self.items[item]

    def check_special(self):
        return 0

# noinspection PyUnusedLocal
# skus = unicode string

offers = Offers()
offers.add_item(Offer("A", 50, "3A for 130"))
offers.add_item(Offer("B", 30, "2B for 45"))
offers.add_item(Offer("C", 20, ""))
offers.add_item(Offer("D", 20, ""))


def checkout(skus):
    print(skus, offers, Counter(skus))


checkout("AAAAABBBCCAAA")




