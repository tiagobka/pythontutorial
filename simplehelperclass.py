"""
Simple helper class
"""
class Person:
    
    # class attributes
    name = ""
    age = 0

    #constructor - first code to run when you instantiate a class
    def __init__(self, name: str, age: int) -> None:
        self.name= name
        self.age = age

    # method section
    def introduce(self)->str:
        return "Hello, my name is {} and I am {} years old".format(self.name, self.age)

    ...












#Notice how if you run this file you get "Hello, my name is Maria and I am 15 years old" but when you import it somewhere it does not run
if __name__ == "__main__":
    Maria= Person("Maria", 15)
    print(Maria.introduce())