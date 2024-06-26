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
    r = re.fullmatch(r'[A-Z]+', skus).group()
    print(r)
    if type(skus) is not str and re.fullmatch(r'[A-Z]+', skus).group() is not None:
        return -1

    counted = Counter(skus)
    total = 0
    for k in counted:
        offer = offers.get_offer(k)
        if offer:
            total += offer.get_total(int(counted[k]))

    return total

print(checkout("a"))
print(checkout("-"))
print(checkout("ABCa"))


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
#     id = CHK_R1_002, req = checkout(""), resp = 0
# id = CHK_R1_003, req = checkout("A"), resp = 50
# id = CHK_R1_004, req = checkout("B"), resp = 30
# id = CHK_R1_005, req = checkout("C"), resp = 20
# id = CHK_R1_006, req = checkout("D"), resp = 15
# id = CHK_R1_007, req = checkout("a"), resp = 0
# id = CHK_R1_008, req = checkout("-"), resp = 0
# id = CHK_R1_009, req = checkout("ABCa"), resp = 100
# id = CHK_R1_010, req = checkout("AxA"), resp = 100
# id = CHK_R1_011, req = checkout("ABCD"), resp = 115
# id = CHK_R1_012, req = checkout("A"), resp = 50
# id = CHK_R1_013, req = checkout("AA"), resp = 100
# id = CHK_R1_014, req = checkout("AAA"), resp = 130
# id = CHK_R1_015, req = checkout("AAAA"), resp = 180
# id = CHK_R1_016, req = checkout("AAAAA"), resp = 230
# id = CHK_R1_017, req = checkout("AAAAAA"), resp = 260
# id = CHK_R1_018, req = checkout("B"), resp = 30
# id = CHK_R1_019, req = checkout("BB"), resp = 45
# id = CHK_R1_020, req = checkout("BBB"), resp = 75
# id = CHK_R1_021, req = checkout("BBBB"), resp = 90
# id = CHK_R1_022, req = checkout("ABCDABCD"), resp = 215
# id = CHK_R1_023, req = checkout("BABDDCAC"), resp = 215
# id = CHK_R1_024, req = checkout("AAABB"), resp = 175
# id = CHK_R1_001, req = checkout("ABCDCBAABCABBAAA"), resp = 505
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







