# 91問目
# x = 10
# try:
#     result = x / 0
# except ZeroDivisionError:
#     print("変数xを0で割ることはできません")

# 92問目
# x = 2
# y = 2
# numbers = [1, 4, 0, 12, 6]

# try:
#     result = y / numbers[x]
#     print(result)
# except IndexError:
#     print("IndexError : リストの要素を超える値が x に設定されています")
# except ZeroDivisionError:
#     print("0で割ることはできません")

# 93問目
# x = 2
# y = 2
# numbers = [1, 4, 0, 12, 6]

# try:
#     result = y / numbers[x]
#     print(result)
# except (IndexError, ZeroDivisionError):
#     print("Errorが発生しました")

# 94問目
# import math

# r = 3
# circle_area = r**2 * math.pi
# print(circle_area)

# 95問目
# import os

# mac = os.getenv("HOME")
# print(mac)

# 96問目
# from datetime import date

# today = date.today()
# print(today)

# 97問目
# from time import sleep

# for number in range(1, 4):
#     print(number)
#     sleep(1)
#     print("1秒Sleepしました")

# 98問目
# from pathlib import Path

# path = Path.cwd()
# print(path)

# 99問目
# from art import text2art

# result = text2art("Learn Python")
# print(result)

# 100問目
# import qrcode

# url = ""
# img = qrcode.make(url)
# img.save("amazon.png")
