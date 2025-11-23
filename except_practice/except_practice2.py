value = 200

if value > 100:
    raise ValueError("value値が100を超えています。")

print("raiseで例外を投げたので、このメッセージは表示されないはずです。")
