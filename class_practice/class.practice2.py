class Customer:

    # 読み取り専用プロパティにする
    def __init__(self, name, age, height, weight):
        self.name = name
        self._age = self._set_age(age)
        self._height = self._set_height(height)
        self._weight = self._set_weight(weight)

    @property
    def bmi(self):
        return self.weight / (self.height / 100) ** 2

    # ageのゲッターとセッター
    # ゲッター内ではプライベート変数にする
    @property
    def age(self):
        return self._age

    # セッター内ではプライベート変数にする
    @staticmethod
    def _set_age(value):
        if not isinstance(value, int):
            raise TypeError("年齢を整数値で入力してください。例:18")
        elif value < 18:
            raise ValueError("18歳未満はご利用いただけません")
        return value

    # heightのゲッターとセッタ
    @property
    def height(self):
        return self._height

    @staticmethod
    def _set_height(value):
        if not isinstance(value, (int, float)):
            raise TypeError("身長を数値で入力してください。例:177")
        elif value < 0:
            raise ValueError("身長正の整数である必要があり、また0は無効値です。")
        return value

    # weightのゲッターとセッタ
    @property
    def weight(self):
        return self._weight

    @staticmethod
    def _set_weight(value):
        if not isinstance(value, (int, float)):
            raise TypeError("体重を数値で入力してください。例:65")
        elif value < 0:
            raise ValueError("体重は正の整数である必要があり、また0は無効値です。")
        return value


yamada = Customer(name="yamada", age=30, height=177, weight=65)
print(yamada.age, yamada.height, yamada.weight, yamada.bmi)
