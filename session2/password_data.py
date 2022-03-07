from typing import TypeVar
# Write your imports here

DIGITS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

# This is a type defined as the PasswordData class
# Only used for static typing and readability
TPasswordData = TypeVar("TPasswordData", bound="PasswordData")

class PasswordData:
    """
    Implement an init method for the PasswordData class.
    This class should take 2 arguments:
        username (str)
        password (str)

    In other words, a class instance will be created by PasswordData(username, password)

    It should have three attributes:
        username            --  Same as argument
        password            --  Same as argument
        encrypted_password  --  This attribute should be an encryption of the
                                password argument. The password can be encrypted
                                using the encrypt_string() function found in the
                                helper_functions module (import required)

    """
    pass # Implement and define your init method here, remove pass
    
    def remove_username_digits(self) -> None:
        """
        Remove any digits in the usename attribute.
        All digits can be found in the constant DIGITS

        Examples
        --------
        1)
        before method:
            username = "this_is_a_pasword123"

        after method:
            username = "this_is_a_password"

        2)
        before method:
            username = "d1i2g3i4t5s21"

        after methods:
            username = "digits"

        Hint:
            the string method replace() might be of use.
        """
        pass # Implement the method here, remove pass

    def __eq__(self, other: TPasswordData) -> bool:
        """
        Implement == operator for objects of PasswordData.
        This "magic" method should check whether the username and password
        of the current instance and another instance are equal.
        Return a boolean
        """
        pass # Implement the method here, remove pass

    def __repr__(self) -> str:
        return f"PasswordData(username={self.username}, password={self.password})"


if __name__ == "__main__":
    pd1 = PasswordData("amazing_cat1337", "this_is_a_strong_password")
    pd1.remove_username_digits()
    
    pd2 = PasswordData("amazing_cat1337", "this_is_a_strong_password")
    print(pd1 == pd2) # This should evaluate to True if __eq__ implemented correctly
    