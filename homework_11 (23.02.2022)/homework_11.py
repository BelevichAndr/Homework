from random import randint, choice
import string
from abc import ABC, abstractmethod  #  TASK 5


class Pet(ABC):
    __counter = 0

    def __init__(self):
        Pet.__counter += 1

    @classmethod
    def get_counter(cls):  # TASK 1
        return cls.__counter

    @staticmethod
    def get_random_name():  # TASK 2
        random_string = f"{choice(string.ascii_uppercase)}-{randint(1, 100)}"
        return random_string

    @abstractmethod
    def voice(self):
        print("base voice")


class Horse(Pet):

    def voice(self):
        print("Horse voice")


class Donkey(Pet):

    def voice(self):
        print("Donkey voice")


class Mule(Donkey, Horse):  # TASK 3
    pass


class Book:  # TASK 4

    def __init__(self, number_of_pages: int, published_year: int, author: str, price: int or float):
        self.__number_of_pages = number_of_pages
        self.__published_year = published_year
        self.__author = author
        self.__price = price

        if not isinstance(number_of_pages, int):
            raise ValueError("Wrong type of 'number_of_pages' ")

        if not isinstance(published_year, int):
            raise ValueError("Wrong type of 'published_year' ")

        if not isinstance(price, (int, float)):
            raise ValueError("Wrong type of 'author' ")

        if not isinstance(number_of_pages, int):
            raise ValueError("Wrong type of 'price' ")



gil = Mule()

print(Pet.get_counter())
print(Pet.get_random_name())
gil.voice()
pischeblock = Book(350, 2018, "Alexey Ivanov", 30)





