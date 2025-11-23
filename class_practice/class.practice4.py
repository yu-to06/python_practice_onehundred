# 抽象クラスの練習

from abc import ABC, abstractmethod


class AbstractAnimal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def walk(self):
        print("抽象クラスのwalkが呼び出されました。")


class Dog(AbstractAnimal):
    def sound(self):
        return "わん"


class Cat(AbstractAnimal):
    def sound(self):
        return "にゃー"


def animal_sound(animal: AbstractAnimal):
    print(animal.sound())


dog = Dog()
cat = Cat()

dog.walk()
animal_sound(dog)
animal_sound(cat)
