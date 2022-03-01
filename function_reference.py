def change_variable(string: str):
    string = "Hamburgare"
    print(f"Id i funktion: {id(string)}")


def pass_value():
    mat = "Korv"
    print(f"Id innan funktion: {id(mat)}")
    change_variable(mat)
    print(f"Mat efter funktion: {mat}")


def change_list(ls: list):
    print(f"Id i funktion: {id(ls)}")
    ls.append("gurka")


def pass_reference():
    veg = ["paprika", "tomat", "sallad"]
    print(f"Id innan: {id(veg)}")

    change_list(veg)
    print(f"Id efter: {id(veg)}")
    print(f"Lista efter funktion: {veg}")


if __name__ == "__main__":
    pass_value()
    # pass_reference()
