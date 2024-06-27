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
specials.add_special("H", [(10, 80), (5, 45)])
specials.add_special("K", [(2, 150)])
specials.add_special("P", [(5, 200)])
specials.add_special("Q", [(3, 80)])
specials.add_special("V", [(3, 130), (2, 90)])

free_specials = FreeSpecial()
free_specials.add_special("E", [(2, "B")])
free_specials.add_special("F", [(3, "F")])
free_specials.add_special("N", [(3, "M")])
free_specials.add_special("R", [(3, "Q")])
free_specials.add_special("U", [(4, "U")])

offers = Offers()
offers.add_item(Offer("A", 50))
offers.add_item(Offer("B", 30))
offers.add_item(Offer("C", 20))
offers.add_item(Offer("D", 15))
offers.add_item(Offer("E", 40))
offers.add_item(Offer("F", 10))

offers.add_item(Offer("G",20))
offers.add_item(Offer("H",10))
offers.add_item(Offer("I",35))
offers.add_item(Offer("J",60))
offers.add_item(Offer("K",80))
offers.add_item(Offer("L",90))
offers.add_item(Offer("M",15))
offers.add_item(Offer("N",40))
offers.add_item(Offer("O",10))
offers.add_item(Offer("P",50))
offers.add_item(Offer("Q",30))
offers.add_item(Offer("R",50))
offers.add_item(Offer("S",30))
offers.add_item(Offer("T",20))
offers.add_item(Offer("U",40))
offers.add_item(Offer("V",50))
offers.add_item(Offer("W",20))
offers.add_item(Offer("X",90))
offers.add_item(Offer("Y",10))
offers.add_item(Offer("Z",50))


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
# print(checkout("UUU"), 120)
print(checkout("STXYZ"), 120)



# id = CHK_R4_003, req = checkout("A"), resp = 50
# id = CHK_R4_004, req = checkout("B"), resp = 30
# id = CHK_R4_005, req = checkout("C"), resp = 20
# id = CHK_R4_006, req = checkout("D"), resp = 15
# id = CHK_R4_007, req = checkout("E"), resp = 40
# id = CHK_R4_008, req = checkout("F"), resp = 10
# id = CHK_R4_009, req = checkout("G"), resp = 20
# id = CHK_R4_010, req = checkout("H"), resp = 10
# id = CHK_R4_011, req = checkout("I"), resp = 35
# id = CHK_R4_012, req = checkout("J"), resp = 60
# id = CHK_R4_013, req = checkout("K"), resp = 80
# id = CHK_R4_014, req = checkout("L"), resp = 90
# id = CHK_R4_015, req = checkout("M"), resp = 15
# id = CHK_R4_016, req = checkout("N"), resp = 40
# id = CHK_R4_017, req = checkout("O"), resp = 10
# id = CHK_R4_018, req = checkout("P"), resp = 50
# id = CHK_R4_019, req = checkout("Q"), resp = 30
# id = CHK_R4_020, req = checkout("R"), resp = 50
# id = CHK_R4_021, req = checkout("S"), resp = 30
# id = CHK_R4_022, req = checkout("T"), resp = 20
# id = CHK_R4_023, req = checkout("U"), resp = 40
# id = CHK_R4_024, req = checkout("V"), resp = 50
# id = CHK_R4_025, req = checkout("W"), resp = 20
# id = CHK_R4_026, req = checkout("X"), resp = 90
# id = CHK_R4_027, req = checkout("Y"), resp = 10
# id = CHK_R4_028, req = checkout("Z"), resp = 50
# id = CHK_R4_029, req = checkout("a"), resp = -1
# id = CHK_R4_030, req = checkout("-"), resp = -1
# id = CHK_R4_031, req = checkout("ABCa"), resp = -1
# id = CHK_R4_032, req = checkout("AxA"), resp = -1
# id = CHK_R4_033, req = checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), resp = 965
# id = CHK_R4_034, req = checkout("A"), resp = 50
# id = CHK_R4_035, req = checkout("AA"), resp = 100
# id = CHK_R4_036, req = checkout("AAA"), resp = 130
# id = CHK_R4_037, req = checkout("AAAA"), resp = 180
# id = CHK_R4_038, req = checkout("AAAAA"), resp = 200
# id = CHK_R4_039, req = checkout("AAAAAA"), resp = 250
# id = CHK_R4_040, req = checkout("AAAAAAA"), resp = 300
# id = CHK_R4_041, req = checkout("AAAAAAAA"), resp = 330
# id = CHK_R4_042, req = checkout("AAAAAAAAA"), resp = 380
# id = CHK_R4_043, req = checkout("AAAAAAAAAA"), resp = 400
# id = CHK_R4_044, req = checkout("P"), resp = 50
# id = CHK_R4_045, req = checkout("PP"), resp = 100
# id = CHK_R4_046, req = checkout("PPP"), resp = 150
# id = CHK_R4_047, req = checkout("PPPP"), resp = 200
# id = CHK_R4_048, req = checkout("PPPPP"), resp = 200
# id = CHK_R4_049, req = checkout("PPPPPP"), resp = 250
# id = CHK_R4_050, req = checkout("PPPPPPP"), resp = 300
# id = CHK_R4_051, req = checkout("PPPPPPPP"), resp = 350
# id = CHK_R4_052, req = checkout("PPPPPPPPP"), resp = 400
# id = CHK_R4_053, req = checkout("PPPPPPPPPP"), resp = 400
# id = CHK_R4_054, req = checkout("UUU"), resp = 120
# id = CHK_R4_055, req = checkout("UUUU"), resp = 120
# id = CHK_R4_056, req = checkout("UUUUU"), resp = 160
# id = CHK_R4_057, req = checkout("UUUUUUUU"), resp = 240
# id = CHK_R4_058, req = checkout("UUUUUUUU"), resp = 240
# id = CHK_R4_059, req = checkout("EE"), resp = 80
# id = CHK_R4_060, req = checkout("EEB"), resp = 80
# id = CHK_R4_061, req = checkout("EEEB"), resp = 120
# id = CHK_R4_062, req = checkout("EEEEBB"), resp = 160
# id = CHK_R4_063, req = checkout("BEBEEE"), resp = 160
# id = CHK_R4_064, req = checkout("RRR"), resp = 150
# id = CHK_R4_065, req = checkout("RRRQ"), resp = 150
# id = CHK_R4_066, req = checkout("RRRRQ"), resp = 200
# id = CHK_R4_067, req = checkout("RRRRRRQQ"), resp = 300
# id = CHK_R4_068, req = checkout("RRRQRQRR"), resp = 300
# id = CHK_R4_069, req = checkout("A"), resp = 50
# id = CHK_R4_070, req = checkout("AA"), resp = 100
# id = CHK_R4_071, req = checkout("AAA"), resp = 130
# id = CHK_R4_072, req = checkout("AAAA"), resp = 180
# id = CHK_R4_073, req = checkout("AAAAA"), resp = 200
# id = CHK_R4_074, req = checkout("AAAAAA"), resp = 250
# id = CHK_R4_075, req = checkout("H"), resp = 10
# id = CHK_R4_076, req = checkout("HH"), resp = 20
# id = CHK_R4_077, req = checkout("HHH"), resp = 30
# id = CHK_R4_078, req = checkout("HHHH"), resp = 40
# id = CHK_R4_079, req = checkout("HHHHH"), resp = 45
# id = CHK_R4_080, req = checkout("HHHHHH"), resp = 55
# id = CHK_R4_081, req = checkout("HHHHHHH"), resp = 65
# id = CHK_R4_082, req = checkout("HHHHHHHH"), resp = 75
# id = CHK_R4_083, req = checkout("HHHHHHHHH"), resp = 85
# id = CHK_R4_084, req = checkout("HHHHHHHHHH"), resp = 80
# id = CHK_R4_085, req = checkout("HHHHHHHHHHH"), resp = 90
# id = CHK_R4_086, req = checkout("HHHHHHHHHHHH"), resp = 100
# id = CHK_R4_087, req = checkout("HHHHHHHHHHHHH"), resp = 110
# id = CHK_R4_088, req = checkout("HHHHHHHHHHHHHH"), resp = 120
# id = CHK_R4_089, req = checkout("HHHHHHHHHHHHHHH"), resp = 125
# id = CHK_R4_090, req = checkout("HHHHHHHHHHHHHHHH"), resp = 135
# id = CHK_R4_091, req = checkout("HHHHHHHHHHHHHHHHH"), resp = 145
# id = CHK_R4_092, req = checkout("HHHHHHHHHHHHHHHHHH"), resp = 155
# id = CHK_R4_093, req = checkout("HHHHHHHHHHHHHHHHHHH"), resp = 165
# id = CHK_R4_094, req = checkout("HHHHHHHHHHHHHHHHHHHH"), resp = 160
# id = CHK_R4_095, req = checkout("V"), resp = 50
# id = CHK_R4_096, req = checkout("VV"), resp = 90
# id = CHK_R4_097, req = checkout("VVV"), resp = 130
# id = CHK_R4_098, req = checkout("VVVV"), resp = 180
# id = CHK_R4_099, req = checkout("VVVVV"), resp = 220
# id = CHK_R4_100, req = checkout("VVVVVV"), resp = 260
# id = CHK_R4_101, req = checkout("B"), resp = 30
# id = CHK_R4_102, req = checkout("BB"), resp = 45
# id = CHK_R4_103, req = checkout("BBB"), resp = 75
# id = CHK_R4_104, req = checkout("BBBB"), resp = 90
# id = CHK_R4_105, req = checkout("NNN"), resp = 120
# id = CHK_R4_106, req = checkout("NNNM"), resp = 120
# id = CHK_R4_107, req = checkout("NNNNM"), resp = 160
# id = CHK_R4_108, req = checkout("NNNNNNMM"), resp = 240
# id = CHK_R4_109, req = checkout("NNNMNMNN"), resp = 240
# id = CHK_R4_110, req = checkout("FF"), resp = 20
# id = CHK_R4_111, req = checkout("FFF"), resp = 20
# id = CHK_R4_112, req = checkout("FFFF"), resp = 30
# id = CHK_R4_113, req = checkout("FFFFFF"), resp = 40
# id = CHK_R4_114, req = checkout("FFFFFF"), resp = 40
# id = CHK_R4_115, req = checkout("K"), resp = 80
# id = CHK_R4_116, req = checkout("KK"), resp = 150
# id = CHK_R4_117, req = checkout("KKK"), resp = 230
# id = CHK_R4_118, req = checkout("KKKK"), resp = 300
# id = CHK_R4_119, req = checkout("Q"), resp = 30
# id = CHK_R4_120, req = checkout("QQ"), resp = 60
# id = CHK_R4_121, req = checkout("QQQ"), resp = 80
# id = CHK_R4_122, req = checkout("QQQQ"), resp = 110
# id = CHK_R4_123, req = checkout("QQQQQ"), resp = 140
# id = CHK_R4_124, req = checkout("QQQQQQ"), resp = 160
# id = CHK_R4_125, req = checkout("V"), resp = 50
# id = CHK_R4_126, req = checkout("VV"), resp = 90
# id = CHK_R4_127, req = checkout("VVV"), resp = 130
# id = CHK_R4_128, req = checkout("VVVV"), resp = 180
# id = CHK_R4_129, req = checkout("H"), resp = 10
# id = CHK_R4_130, req = checkout("HH"), resp = 20
# id = CHK_R4_131, req = checkout("HHH"), resp = 30
# id = CHK_R4_132, req = checkout("HHHH"), resp = 40
# id = CHK_R4_133, req = checkout("HHHHH"), resp = 45
# id = CHK_R4_134, req = checkout("HHHHHH"), resp = 55
# id = CHK_R4_135, req = checkout("HHHHHHH"), resp = 65
# id = CHK_R4_136, req = checkout("HHHHHHHH"), resp = 75
# id = CHK_R4_137, req = checkout("HHHHHHHHH"), resp = 85
# id = CHK_R4_138, req = checkout("HHHHHHHHHH"), resp = 80
# id = CHK_R4_139, req = checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"), resp = 1880
# id = CHK_R4_140, req = checkout("LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH"), resp = 1880
# id = CHK_R4_141, req = checkout("AAAAAPPPPPUUUUEEBRRRQAAAHHHHHHHHHHVVVBBNNNMFFFKKQQQVVHHHHH"), resp = 1640
# id = CHK_R4_001, req = checkout("PPPPQRUVPQRUVPQRUVSU"), resp = 740



