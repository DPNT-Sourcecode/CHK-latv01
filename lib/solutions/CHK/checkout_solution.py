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
            return 0, value

class FreeSpecial(Specials):
    def __init__(self):
        super().__init__()

    def get_special(self, key, value):
        if key in self.items:
            ret = []
            for v in self.items[key]:
                covered = int(value) // v[0]
                if covered > 0:
                    ret.append(v[1])
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

specials.add_special("A", [ (3, 130)])
specials.add_special("B", [(2, 45)])

free_specials = FreeSpecial()
free_specials.add_special("E", [(2, "B")])

offers = Offers()
offers.add_item(Offer("A", 50))
offers.add_item(Offer("B", 30))
offers.add_item(Offer("C", 20))
offers.add_item(Offer("D", 15))
# offers.add_item(Offer("E", 40))


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

    for fi in free_items:
        if fi in counted and counted[fi] > 0:
            counted[fi] -= 1

    for k in counted:
        offer = offers.get_offer(k)
        if offer:
            total += offer.get_total(int(counted[k]), specials)

    return total

print(checkout(""))
print(checkout("-"))
print(checkout("AAAAAAAABCDEE"))
print(checkout("a"))
print(checkout("-"))
print(checkout("ABCa"))

print(checkout("A"), 50)
print(checkout("B"),  30)
print(checkout("C"),  20)
print(checkout("D"),  15)
print(checkout("ABCa"),  100)
print(checkout("AxA"),  100)
print(checkout("ABCD"), 115)
print(checkout("A"), 50)
print(checkout("AA"), 100)
print(checkout("AAA"), 130)
print(checkout("AAAA"), 180)
print(checkout("AAAAA"), 230)
print(checkout("AAAAAA"), 260)
print(checkout("B"), 30)
print(checkout("BB"), 45)
print(checkout("BBB"), 75)
print(checkout("BBBB"), 90)
print(checkout("ABCDABCD"), 215)
print(checkout("BABDDCAC"), 215)
print(checkout("AAABB"), 175)
print(checkout("ABCDCBAABCABBAAA"),  505)


# - {"method":"checkout","params":["a"],"id":"CHK_R1_007"}, expected: -1, got: 0
# - {"method":"checkout","params":["-"],"id":"CHK_R1_008"}, expected: -1, got: 0
# - {"method":"checkout","params":["ABCa"],"id":"CHK_R1_009"}, expected: -1, got: 100
#
# /Users/alekschervinsky/Downloads/accelerate_runner/venv/bin/python /Users/alekschervinsky/Downloads/accelerate_runner/lib/send_command_to_server.py
# 50
# 100
# 130
# 180
# 360
# Connecting to run.accelerate.io
#
# Your progress (2/3):
# ✓ SUM (1 round)  -   warmup - completed in 8 min (+0 min penalty)
# ✓    └── SUM_R1  - completed in 8 min (+0 min penalty)
# ✓ HLO (2 rounds) -   warmup - completed in 7 min (+10 min penalty)
# ✓    ├── HLO_R1  - completed in 4 min (+10 min penalty)
# ✓    └── HLO_R2  - completed in 2 min (+0 min penalty)
# @ CHK (5 rounds) - official - Supermarket checkout
# >    ├── CHK_R1  - running for 42 min (+10 min penalty)
# ├── CHK_R2  - not started
# ├── CHK_R3  - not started
# ├── CHK_R4  - not started
# └── CHK_R5  - not started
# ---------------------
#
# Type "deploy" if you have answered all the requests.
# Type "pause" if you need a break.
#
# > deploy
# Selected action is: deploy
# Starting client
# Waiting for requests
#     id = CHK_R1_002, req = checkout(""), 0
# print(checkout("A"), 50)
# print(checkout("B"), 30)
# print(checkout("C"), 20)
# print(checkout("D"), 15)
# print(checkout("a"), 0)
# print(checkout("-"), 0)
# print(checkout("ABCa"), 100
# print(checkout("AxA"), 100
# print(checkout("ABCD"), 115
# print(checkout("A"), 50
# print(checkout("AA"), 100
# print(checkout("AAA"), 130
# print(checkout("AAAA"), 180
# print(checkout("AAAAA"), 230
# print(checkout("AAAAAA"), 260
# print(checkout("B"), 30
# print(checkout("BB"), 45
# print(checkout("BBB"), 75
# print(checkout("BBBB"), 90
# print(checkout("ABCDABCD"), 215
# print(checkout("BABDDCAC"), 215
# print(checkout("AAABB"), 175
# print(checkout("ABCDCBAABCABBAAA"), 505)
# Stopping client
# Notify round "CHK_R1", event "deploy"
# --------------------------------------------
#
# Result is: FAILED
# Some requests have failed (4/24). Here are some of them:
# - {"method":"checkout","params":["a"],"id":"CHK_R1_007"}, expected: -1, got: 0
# - {"method":"checkout","params":["-"],"id":"CHK_R1_008"}, expected: -1, got: 0
# - {"method":"checkout","params":["ABCa"],"id":"CHK_R1_009"}, expected: -1, got: 100
# You have received a penalty of: 10 min
# The round will restart now
#
# Look at your failed trials and edit your code. When you've finished, deploy your code with "deploy"
#
# Challenge description saved to file: challenges/CHK_R1.txt.
#
# Process finished with exit code 0

