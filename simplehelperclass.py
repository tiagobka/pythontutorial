"""
Simple helper class
"""


class person:
    name = ""
    age = 0

    def __init__(self, name: str, age: int) -> None:
        self.name= name
        self.age = age

    def introduce(self)->str:
        return "Hello, my name is {} and I am {} years old".format(self.name, self.age)


#Notice how if you run this file you get "Hello, my name is Maria and I am 15 years old" but when you import it somewhere it does not run
if __name__ == "__main__":
    Maria= person("Maria", 15)
    print(Maria.introduce())