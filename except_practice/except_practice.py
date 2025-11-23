# 例外処理の練習
try:
    num = int(input("整数値を入力してください"))
    result = 10 / num
except ValueError as e:
    print(f"数値を入力してください {e}")
except ZeroDivisionError as e:
    print(f"0は入力できません {e}")
else:
    print(result)
finally:
    print("処理が完了しました")
