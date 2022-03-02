# Variables, int, floats and strings
def variables():
    a = "Python"  # Points to same memory location
    b = "Python"

    id(a)
    id(b)

    a is b

    int1 = 5
    int2 = 5

    float1 = 5.0
    kvot = 5 // 2  # Floor division

    a, b = 5, 6  # Multiple assignment

    python_string = "\npython\n is great!"  # Naming convension
    CAPITAL_LETTERS = "this is a constant by convension"

    print(int1 == float1)

    print("Python" == "Python")


###############################################################################
# Standard output
def stdout():
    string = "hej x "
    integer = 2
    print(string, integer)
    print("Hello world")  # New line automatically
    print_out = f"jag säger {string} {integer} gånger"
    print(print_out)


###############################################################################
# Strings
def strings():
    # Indexing
    s = "Python"
    s[0]
    s[0:3]
    s[:3]
    s[3:]
    s[len(s) - 1]
    s[-1]

    # Concatenation (sammanlänkning)
    vem = "jag "
    gör = "äter "
    vad = "friscomål"
    handling = vem + gör + vad

    handling = vem + gör + vad[0:7] + vad[7] * 10 + vad[7:]
    print(handling)

    dir(s)
    c = "R".lower()


###############################################################################
# Functions
def print_last_two_letters(word: str) -> None:
    print(word[-3:])  # Indentation


def magic_food(number: int, food: str) -> str:
    print(f"Jag har {number} av {food}")
    number += 10  # Pass by value
    return f"Nu har jag {number} av {food}. MAGISKT!"


if __name__ == "__main__":
    nr_of_food = 10
    food = "avocado"
    new_nr_of_food = magic_food(nr_of_food, food)
    print(new_nr_of_food)
    print_last_two_letters("hejdå")
