class Supermarket:

    # Initialize class attributes
    def __init__(self, name: str, address: str, size: int):
        # Attributes
        self.name = name
        self.address = address
        self.size = size
        print("Creating a new instance of supermarket")
    #################################################
    # Methods
    def change_size(self):
        self.size *= 2

    # Magic methods
    def __repr__(self):
        return f"Supermarket(name={self.name}, self.address={self.address}, self.size={self.size})"


if __name__ =="__main__":
    supermarket1 = Supermarket(name="ICA", address="matgatan 1", size=200)
    supermarket2 = Supermarket(name="COOP", address="matgatan 2", size=300)
    