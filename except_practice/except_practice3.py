def get_number():
    while True:
        try:
            num = int(input("数字を入力してください"))
        except ValueError:
            print("再度数字を入力してください")
        except KeyboardInterrupt:
            print("入力がキャンセルされました")
            break
        else:
            return num


input_num = get_number()
print(f"あなたが入力した数値の2乗は{input_num ** 2} です")
