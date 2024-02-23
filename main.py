from macro_dyn import add_two_numbers, macro_dyn

def main():
    md = macro_dyn\
    ( 
        phi=1,
        g=1.0,
        theta1=0.5
    )
    md.some_value = 10

    md.update_params()

    print("psi", md.psi)
    print("rhoxp", md.rhoxp)
    print("rhoxm", md.rhoxm)

    # since the person (Mike, 27 yo) was created(instantiated in init) you can use it
    print(md.person.introduce())

    print(add_two_numbers(5,7))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()