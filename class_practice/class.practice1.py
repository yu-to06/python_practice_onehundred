class Human:
    populations = "8 billion"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello! My name is {self.name} and \n I am {self.age} years old")


yamada = Human(name="yamada", age=16)

# クラス変数はインスタン化しなくても呼び出せる。
# print(
#     f"Human class's population value is {Human.populations}. and \n yamada instance's population is {yamada.populations}"
# )

#  hasattr(object , 属性名)
print(hasattr(yamada, "name"))

# getattr(object , 属性名)
print(getattr(yamada, "age"))

# setattr(object , 属性名 , 属性値)
setattr(yamada, "address", "Tokyo")
print(yamada.address)
