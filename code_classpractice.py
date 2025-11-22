class User:
    def __init__(self, name, mail_address, point):
        self.name = name
        self.mail_address = mail_address
        self.point = int(point)

    # ポイント追加メソッド
    def add_point(self, point):
        self.point += point


# 佐藤さんと小林さんのユーザーオブジェクト
user_sato = User("佐藤", "abc@example.com", 1500)
user_kobayashi = User("小林", "xyz@example.com", 3000)

# 佐藤さんのポイントを100追加
user_sato.add_point(100)
print(user_sato.point)
