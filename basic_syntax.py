# TODO
# Nested functions and yield
# Add documentation to every exercise
# Possible additions in future:
#   - Multiple function return values
#   - Default values
#   - More types, like float. Could create function to determine how "strong" password is
#   - zip?

# Basic syntax, loops, conditional statements and strings
# Content:
# - print() and string formatting
#   getting_started()
#
# - String manipulaiton, indexing and operators
#   upper_encryption(), swap_encryptions()

from cryptography.fernet import Fernet
import random

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

INVALID_CHARACTERS = (
    ".",
    "\\",
    "\n",
    "@",
    "!",
    "?",
    "=",
    "'",
    "*",
    "<",
    ">",
    "#",
    "%",
    "&",
    "(",
    ")",
    "{",
    "}",
)


def getting_started(name: str) -> None:
    """
    Print the following text:

    Welcome to python: "<name>". Here is the address of your name: <address>.
    The adress is of type: <type>.

    Where:
        <name>      - input argument
        <address>   - integer address of name
        <type>      - type of address (should be <class 'int'>)

    As special characters, the text should contain a newline and quotation marks around name.
    """
    print(
        f'Welcome to python: "{name}". Here is the address of your name: {id(name)}.\nThe adress is of type: {type(id(name))}'
    )


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
    return password + password[-2].upper()


def swap_encryption(password: str) -> str:
    """
    Encrypt a password by swaping the first and second half of the password string.
    The chracter swap should be made around the middle point of the string.
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
    middle = len(password) // 2
    return password[middle:] + password[:middle]


# Encrypt a password string
def encrypt(password: str) -> str:
    return swap_encryption(upper_encryption(password))


# Return a string of invalid characters
def invalid_characters(username: str) -> list:
    return [char for char in INVALID_CHARACTERS if char in username]


# Add a unique password to a list of passwords
def add_to_list(password: str, encrypted_passwords: list) -> None:
    encrypted_password = encrypt(password)
    for list_password in encrypted_passwords:
        if encrypted_password == list_password[1]:
            list_password[0] += 1
            return

    encrypted_passwords.append([1, encrypted_password])


# Encrypt a string a passwords separated by a newline
def encrypt_multiple_passwords(passwords: str) -> list:
    encrypted_password_list = []
    for password in passwords.split():
        add_to_list(password, encrypted_password_list)

    return encrypted_password_list


# Return list of unique passwords
def unique_passwords(passwords: str) -> str:
    return "\n".join(set(passwords.split()))


# Generate a random password based on letters and numbers
def generate_password() -> str:
    ps_len = random.randrange(10, 20)
    password = ""
    for _ in range(ps_len):
        password += random.choice(ABC123)

    return password


# <service>;<username>;<password>
def create_password_dict(csv_file: str) -> dict:
    line_list = csv_file.split()
    password_dict = {}
    for line in line_list:
        service, username, password = line.split(";")
        if len(password) == 0:
            password = generate_password()
        else:
            password = encrypt(password)

        if len(invalid_characters(username)) == 0:
            password_dict[service] = (username, password)

    return password_dict


# Check if password is greater than 6 and less than 66 characters.
# Also check if last character
def check_password_length(password):
    return True if 6 <= len(password) <= 80 else False


if __name__ == "__main__":
    print(swap_encryption("pass_word"))
