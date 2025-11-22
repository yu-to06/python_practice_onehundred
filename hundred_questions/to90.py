# 81問目
# import random


# class Card:
#     def __init__(self, suit, number):
#         self.suit = suit
#         self.number = number


# class Deck:
#     def __init__(self):
#         self.cards = []
#         for suit in ["ハート", "ダイヤ", "スペード", "クラブ"]:
#             for number in range(1, 14):
#                 card = Card(suit, number)
#                 self.cards.append(card)

#     def shuffle(self):
#         random.shuffle(self.cards)

#     def draw_card(self):
#         return self.cards.pop(5)


# deck = Deck()
# deck.shuffle()
# for _ in range(5):
#     drawn_card = deck.draw_card()
#     print(f"{drawn_card.suit}の{drawn_card.number}")

# 82問目
# from module import add

# result = add(1, 2)
# print(result)

# 83問目
# from module import Card, URL

# card = Card(suit="heart", number=1)
# url = URL
# print(f"このカードのsuitは{card.suit}で数字は{card.number}です。URLは{url}です")

# 84問目
# import module

# result = module.add(1,2)
# print(result)

# 85問目
# from my_packages.module import add

# print(add(1, 2))

# 86問目
# 書き込みモードは w
# text = "Hello World"

# with open(
#     "/Users/uchidatoshinori/python_vs_practice/hundred_questions/doc.txt", "w"
# ) as f:
#     f.write(text)


# 87問目
# 追記モードは a
# text = "goodbye World"
# with open(
#     "/Users/uchidatoshinori/python_vs_practice/hundred_questions/doc.txt", "a"
# ) as f:
#     f.write(f"\n{text}")

# 88問目
# 読み取りモードは r
# with open(
#     "/Users/uchidatoshinori/python_vs_practice/hundred_questions/doc.txt", "r"
# ) as f:
#     text = f.read()
# print(text)

# 89問目
# リスト化するメソッド
# with open(
#     "/Users/uchidatoshinori/python_vs_practice/hundred_questions/doc.txt", "r"
# ) as f:
#     lines = f.readlines()
# print(lines)

# 90問目
# x = 10
# result = x / 0
# print(result)
