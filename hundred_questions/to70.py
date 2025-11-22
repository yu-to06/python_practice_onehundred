# 61問目
# text = "あかさたな-はまやらわ"
# for char in text:
#     if char == "-":
#         break
#     print(char)

# 62問目
# ng_numbers = [4, 9, 13]
# for number in range(1, 21):
#     if number in ng_numbers:
#         continue
#     print(number)

# 63問目
# for number in range(1, 21):
#     if number % 3 == 0:
#         print(f"{number}は3の倍数です")
#     else:
#         print(number)

# 64問目
# addresses = {
#     "山田": "xxx@example.com",
#     "佐藤": "yyy@gmail.com",
#     "鈴木": "zzz@yahoo.co,jp",
# }
# gmail_addresses = {}
# for name, email in addresses.items():
#     if email.endswith("gmail.com"):
#         gmail_addresses[name] = email
# print(gmail_addresses)

# 65問目
# for i in range(1,10):
#     for j in range(1,10):
#         print(f"{i}x{j}={i*j}")


# 66問目
# def hello_function(text):
#     print(f"Hello,{text}!")


# hello_function("Python")


# 67問目
# def add(a, b):
#     return a + b


# print(add(a=10, b=20))


# 68問目
# numbers = [14, 32, 80, 1, 9]


# def sum_and_avg(number_list):
#     total = sum(number_list)
#     average = total / len(number_list)
#     return total, average


# print(sum_and_avg(numbers))

# 69問目
# numbers = [14, 32, 80, 1, 9]


# def is_even(number):
#     return number % 2 == 0


# for num in numbers:
#     if is_even(num):
#         print(f"{num}は偶数です")
#     else:
#         print(f"{num}は奇数です")


# 70問目
# def drink_price(drink_size, has_whip=False):
#     price = 0
#     if drink_size == "S":
#         price += 100
#     elif drink_size == "M":
#         price += 200
#     elif drink_size == "L":
#         price += 300
#     if has_whip:
#         price += 100
#     return price


# Mprice_and_whip = drink_price("M", True)
# Lpcrice_no_whip = drink_price("L", False)
# print(f"Mサイズのドリンクにホイップをつけた場合、{Mprice_and_whip}円です")
# print(f"Lサイズのドリンクにホイップをつけない場合、{Lpcrice_no_whip}円です")
