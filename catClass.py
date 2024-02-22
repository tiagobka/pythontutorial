from animalClass import Animal


class Cat (Animal):

    def __init__(self, name) -> None:
        super().__init__(name)

    def jump(self)-> None:
        self.hungry = True
        print("{} jumped".format(self.name))