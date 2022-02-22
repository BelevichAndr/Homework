class Pet:
    def __init__(self, name='Unknown'):
        self.__name = name

    def get_name(self):
        return self.__name


class Cat(Pet):
    def meow(self):
        print('мяу')


class Dog(Pet):
    def gav(self):
        print('Гав!')
