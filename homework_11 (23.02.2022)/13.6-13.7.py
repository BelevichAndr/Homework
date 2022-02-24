# TASKS 13.6 AND 13.7(1)
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def voice(self):
        print('Animal voice')


class Feline(ABC):
    @abstractmethod
    def feline_animal_type(self):
        raise NotImplemented


class Canine(ABC):
    @abstractmethod
    def canine_animal_type(self):
        raise NotImplemented


class Pet(Animal):
    def voice(self):
        print('Pet voice')


class WildAnimal(Animal):
    def voice(self):
        print('WildAnimal voice')


class Cat(Pet, Feline):
    def voice(self):
        print('Cat voice')

    def feline_animal_type(self):
        print("Feline")


class Dog(Pet,Canine):
    def voice(self):
        print('Dog voice')

    def canine_animal_type(self):
        print("Canine")


class Lion(Pet, Feline):
    def voice(self):
        print('Lion voice')

    def feline_animal_type(self):
        print("Feline")


class Wolf(Pet, Canine):
    def voice(self):
        print('Wolf voice')

    def canine_animal_type(self):
        print("Canine")



a = Pet()
b = Wolf()
a.voice()
b.canine_animal_type()
b.voice()
