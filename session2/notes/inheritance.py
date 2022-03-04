from object_oriented_programming import Supermarket


class SuperSuperMarket(Supermarket):
    def __init__(self, name: str, address: str, size: int, levels: int):
        # First way of doing it
        # Supermarket.__init__(self, name, address, size)

        # Right way to do it
        super().__init__(name, address, size)

        self.size = levels * size
        self.__levels = levels

    def double_size(self):
        # What will size be when we inherit the method from the parent?
        self.size = super().double_size()

    # Private attribute
    def get_levels(self):
        return self.__levels


def inheritance():
    supersupermarket1 = SuperSuperMarket("ica", "matgatan 4", size=200, levels=2)
    # Can still access methods and attributres from the parent
    print(supersupermarket1.size)

    # Show what will happen with the inherited method
    supersupermarket1.double_size()

    # Private attributes, make levels private
    print(SuperSuperMarket.__levels)
    print(supersupermarket1.get_levels())

    # Mention protected attributes is there is time


if __name__ == "__main__":
    inheritance()
