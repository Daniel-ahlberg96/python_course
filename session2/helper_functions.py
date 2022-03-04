from random import randrange, choice, shuffle

ABC123 = (
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
)


def generate_password() -> str:
    """
    Generate a password with random characters and numbers.

    Return:
        Generated password
    """
    ps_len = randrange(10, 20)
    password = ""
    for _ in range(ps_len):
        password += choice(ABC123)

    return password


def encrypt_string(string: str) -> str:
    """
    Encrypt a string.

    Keyword arguments:
        string -- the string to be encrypted

    Return:
        An encrypted string
    """

    ls = list(string)
    shuffle(ls)
    encrypted_string = ""
    for char in ls:
        encrypted_string += char + choice(ABC123)

    return encrypted_string


if __name__ == "__main__":
    # generate_password()
    print(encrypt_string("test"))
