from supermarket import Supermarket


class SuperSuperMarket(Supermarket):
    def __init__(self, name: str, address: str, size: int, levels: int):
        # First way of doing it
        Supermarket.__init__(self, name, address, size)

        # Right way to do it
        # super().__init__(name, address, size)


    def __repr__(self):
        return f"SuperSupermarket(name={self.name}, address={self.address}, size={self.size}, levels={self.__levels})"


if __name__ == "__main__":
    supersupermarket1 = SuperSuperMarket("ica", "matgatan 4", size=200, levels=2)

