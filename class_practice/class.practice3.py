# 継承の練習
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello {self.name}san , Are you {self.age} years old?"

    def __str__(self):
        return f"My name is {self.name}"


class Customer(Human):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

    def greet(self):
        base_greet = super().greet()
        return f"{base_greet} \nAre you living in {self.address}?"


taro = Customer(name="Taro", age=18, address="TOKYO")
print(taro.greet())
print(taro.__str__())
