def imports():
    import math # Import an entire module
    math.pi # Namespace

    from math import pi # Specific function

    import helper_functions # File name
    
    helper_functions.ABC123 # Constant in file
    from helper_functions import ABC123, example_function # Multiple imports

    print(ABC123)

# #######################################################
# Object oriented programming, what a class is, __init__
def bad_way_of_representing_data():
    food = {
        "ICA": ["matgatan 1", 200],
        "COOP": ["matgatan 2", 300]
    }  # Ugly, better way to generalizing data?

    ica_property = food["ICA"]
    food["Willys"] = ica_property
    del food["ICA"]
    print(food)


class Supermarket:
    sales = "food"  # Class variable

    # Initialize class attributes
    def __init__(self, name: str, address: str, size: int):
        # Attributes
        self.name = name
        self.address = address
        self.size = size
        # Talk about extra variables if there is time
        self.types_of_food = "vegetables"
        print("Creating a new instance of supermarket")

    #################################################
    # Methods
    def change_size(self):  # Does everyone understand what a method is?
        self.size *= 2

    # Magic methods
    def __repr__(self):
        return f"Supermarket(name={self.name}, self.address={self.address}, self.size={self.size})"

    def __gt__(self, other):
        return self.size > other.size


def class_attributes():
    # Self is not a argument we provide to the class, it is default
    supermarket1 = Supermarket(name="ICA", address="matgatan 1", size=200)
    supermarket2 = Supermarket(name="COOP", address="matgatan 2", size=300)

    print(supermarket1.name, supermarket2.name)

    supermarket1.name = "Willys"

    print(supermarket1.name, supermarket2.name)


def methods():
    supermarket1 = Supermarket(name="ICA", address="matgatan 1", size=200)
    print(dir(supermarket1))

    # Implement double_size()
    supermarket1.change_size()
    print(supermarket1.size)

    print(repr({"mat": "ica"}))

    # Implement __repr__()
    print(repr(supermarket1))  # Useful for debuggning
    print(str(supermarket1))  # Convert to string, we get a object representation

    supermarket2 = Supermarket(name="COOP", address="matgatan 2", size=300)

    print(supermarket1 > supermarket2)

    # Implement __gt__()
    print(supermarket1 > supermarket2)


if __name__ == "__main__":
    bad_way_of_representing_data()
    methods()
    
