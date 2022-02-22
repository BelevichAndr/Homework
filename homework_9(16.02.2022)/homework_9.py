class Pet:
    __counter = 0

    def __init__(self, height, weight, name, age, master='Andrei', address='Minsk'):
        self.height = height
        self.weight = weight
        self.__name = name
        self.__age = age
        self.__master = master
        self.__address = address
        Pet.__counter += 1

    def change_weight(self, value=0.2):
        self.weight += value

    def change_height(self, value=0.2):
        self.height += value

    def jump(self, value):
        print(f'Jump {value} meters')

    def voice(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, value):
        self.__master = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value


class Dog(Pet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def voice(self):
        print('Bark!')

    def jump(self, value):
        if value > 0.5:
            print('Dogs cannot jump so high')
        else:
            print(f'Jump {value} meters')


class Cat(Pet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def voice(self):
        print('meow!')

    def jump(self, value):
        if value > 2:
            print('Cats cannot jump so high')
        else:
            print(f'Jump {value} meters')


class Parrot(Pet):
    def __init__(self, species, *args, **kwargs):
        self.species = species
        super().__init__(*args, **kwargs)

    def fly(self):
        if self.height > 0.1:
            print('This parrot cannot fly.')
        else:
            print('fly!')

    def voice(self):
        print("I'm very smart Parrot")

    def change_weight(self, value=0.05):
        self.weight += value

    def change_height(self, value=0.05):
        self.height += value

    def jump(self, value):
        if value > 0.05:
            print('Parrots cannot jump so high')
        else:
            print(f'Jump {value} meters')


rex = Dog(50, 20, 'rex', 5)
barsik = Cat(50, 10, 'barsik', 6)
jec = Parrot('Red', 50, 1, 'jac', 5)

pets = [rex, barsik, jec]


def pet_voice(pets):
    for pet in pets:
        pet.voice()


pet_voice(pets)
print(jec._Pet__counter)
