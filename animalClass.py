class Animal:
    name = ""
    hungry = True

    def __init__(self, name)-> None:
        self.name = name
        print("{} is hungry".format(name))

    def eat(self)->None:
        self.hungry = False
        print("{} is not hungry anymore".format(self.name))
    
    def isHungry(self)->bool:
        return self.hungry