import math


def upper_encryption(password: str) -> str:
    """
    Convert the second to last character in password to uppercase.
    Then add this character to the existing password and return the result

    Examples
    ------------
    1)
    function input:
        password = "password"

    function output:
        "passwordR"

    2)
    function input:
        password = "a_random_string"

    function output:
        "a_random_stringN"

    Hint:
    dir("") can be used to check string methods. Does anything look like uppercase?

    """
    # Write your code here
    new_password = password + password[-2].upper()
    print(new_password)
    return new_password


def swap_encryption(password: str) -> str:
    """
    Encrypt a password by swapping the first and second half of the password string.
    The character swap should be made around the middle point of the string.
    The middle point of a string with uneven length is the floor of the string length divided by 2.
    Return the result of this swap

    Examples
    ------------
    1)
    function input:
        password = "password"

    function output:
        "wordpass"

    2)
    function input:
        password = "pass_word"

    function output:
        "_wordpass"
    """
    # Write your code here
    idx = len(password) // 2
    new_password = password[idx:] + password[:idx]
    print(new_password)
    return new_password


if __name__ == "__main__":
    # upper_encryption("test")
    swap_encryption("test")
    swap_encryption("test2")
