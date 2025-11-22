# for練習
scores = [90, 85, 78, 92, 88]
numbers = [10, 21, 101, 89, 43]
names = ["山田", "鈴木", "加藤"]


subjets_and_scores = [
    ("Math", 90),
    ("English", 85),
    ("Science", 78),
    ("History", 92),
    ("Art", 88),
]

# リストの場合は変数が一つで良い
for score in scores:
    print(f"your score is {score}")

for name in names:
    print(f"hello, {name} san!")

# 辞書の場合は変数が key と value の二つ必要
for subjet, score in subjets_and_scores:
    print(f"your {subjet} score is {score}")

# rangeを使ったfor文 0~4が表示される
for number in range(5):
    print(f"number is {number}")
