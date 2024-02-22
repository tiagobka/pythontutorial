
from helperfunctions import sum_two_numbers, say_hello_world

from simplehelperclass import person
import secondwaytousehelperfunctions as np #<--- can give any name for shortening the long name (used for numpy for instance)
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    say_hello_world()

    np.say_hello()
    np.say_hi()

    print(sum_two_numbers(1, 1))

    #instantiate a person:
    Jonh = person("John", 26)
    Anna = person("Anna", 32)

    print(Anna.introduce())
    print(Jonh.introduce())


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()