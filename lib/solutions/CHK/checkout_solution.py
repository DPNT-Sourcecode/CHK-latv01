
class Offer:
    def __init__(self, item, price, special):
        self.item = item
        self.price = price
        self.special = special



Our price table and offers:
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
    | B    | 30    | 2B for 45      |
    | C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    print(skus)

checkout("AAAAABBBCCAAA")



