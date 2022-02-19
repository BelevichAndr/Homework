class Dog:
    def __init__(self, height, weight, name, age, master='Andrei'):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.__master = master

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def bark(self):
        print('Bark!')

    def change_name(self, new_name):
        self.name = new_name

    def get_master(self):
        return self.__master


rex = Dog(50, 20, 'rex', 5)
muhtar = Dog(60, 25, 'muhtar', 6)
print(muhtar.get_master())


