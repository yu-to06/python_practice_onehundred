# 71問目
# JP_MONTHS = {
#     1: "睦月",
#     2: "如月",
#     3: "弥生",
#     4: "卯月",
#     5: "皐月",
#     6: "水無月",
#     7: "文月",
#     8: "葉月",
#     9: "長月",
#     10: "神無月",
#     11: "霜月",
#     12: "師走",
# }


# def print_jp_months(num):
#     print(f"{num}月は{JP_MONTHS[num]}です")


# print_jp_months(3)
# print_jp_months(12)

# 72問目
# words = ["Apple", "banana", "Cherry", "lemon"]


# def modify_words(word):
#     first_char = word[0]
#     if first_char.isupper():
#         return word.upper()
#     else:
#         return word


# modified_words = []
# for word in words:
#     m_word = modify_words(word)
#     modified_words.append(m_word)
# print(modified_words)


# 73問目
# class Student:
#     def __init__(self):
#         self.name = ""
#         self.grade = 1
#         self.section = "A"
#         self.scores = {}


# 74問目
# class Student:
#     def __init__(self, name, grade, section):
#         self.name = name
#         self.grade = grade
#         self.section = section
#         self.scores = {}


# student = Student(name="Suzuki", grade=2, section="B")
# print(student.name)


# 75問目
# class Student:
#     def __init__(self, name, grade, section):
#         self.name = name
#         self.grade = grade
#         self.section = section
#         self.scores = {}

#     def add_score(self, subject, score):
#         self.scores[subject] = score


# student = Student(name="Suzuki", grade=2, section="B")
# student.add_score(subject="Math", score=80)
# student.add_score(subject="English", score=90)

# print(student.scores)


# 76問目
# class Student:
#     def __init__(self, name, grade, section):
#         self.name = name
#         self.grade = grade
#         self.section = section
#         self.scores = {}

#     def add_score(self, subject, score):
#         self.scores[subject] = score

#     def total_score(self):
#         return sum(self.scores.values())


# student = Student(name="Suzuki", grade=2, section="B")
# student.add_score(subject="Math", score=80)
# student.add_score(subject="English", score=90)
# print(student.total_score())


# 77問目
# class Student:
#     def __init__(self, name, grade, section):
#         self.name = name
#         self.grade = grade
#         self.section = section
#         self.scores = {}

#     def add_score(self, subject, score):
#         self.scores[subject] = score

#     def total_score(self):
#         return sum(self.scores.values())


# student = Student(name="Suzuki", grade=2, section="B")
# student.grade = 3
# student.section = "C"
# print(f"grade is {student.grade} and section is {student.section}")


# 78問目
# class Student:
#     def __init__(self, name, grade, section, scores):
#         self.name = name
#         self.grade = grade
#         self.section = section
#         self.scores = scores

#     def add_score(self, subject, score):
#         self.scores[subject] = score

#     def total_score(self):
#         return sum(self.scores.values())


# student1 = Student(
#     name="Suzuki", grade=2, section="B", scores={"Math": 80, "English": 90}
# )
# student2 = Student(
#     name="Takahashi", grade=1, section="A", scores={"Math": 70, "English": 85}
# )
# student3 = Student(
#     name="Tanaka", grade=3, section="C", scores={"Math": 90, "English": 95}
# )

# for student in [student1, student2, student3]:
#     print(f"{student.name}'s total score is {student.total_score()}")

# 79問目
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
#         return self.cards.pop(0)


# 80問目
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
#         return self.cards.pop(0)


# deck = Deck()
# deck.shuffle()
# for card in deck.cards:
#     print(f"{card.suit}{card.number}")
