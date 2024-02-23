from simplehelperclass import Person
class macro_dyn:
    # example of using contructor (__init__) to set class attributes

    phi: float                  # smoothing parameter for consumption 
    g:int                      # consumption growth rate
    theta1: float

    # for variables that are known and will likelly not change their values you can define them like this
    theta2:float =5      
    gamma:float = 9

    #example of assigning a value to an attribute outside the constructor. (See main)
    some_value:int

    #example of using another class within this
    person: Person

    def __init__(self, phi, g, theta1) -> None:
            self.phi = phi
            self.g = g
            self.theta1 = theta1

            self.person = Person("Mike", 27)

    def update_params(self) -> None:
        self.rhoxp = 1/(self.phi - self.theta1)
        self.rhoxm = self.theta2/(self.phi - self.theta1)
        self.psi    = 1/(self.gamma*(self.phi - self.theta1))


    #creates new attributes (class variables)
    def example_create_new_attributes(self):
         self.name = "Rudolph"
         self.pi  = 3.14159





#can have multiple classes in a file
class newclass:
     
     name:str
     age:int

     


      

#can also have functions in the same file - they are called helper functions
#notice how it does not need self in the parameter
def add_two_numbers(a:int, b:int):
     return a + b
     