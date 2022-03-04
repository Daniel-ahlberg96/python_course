import random
from constants import INVALID_CHARACTERS, ABC123


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
    middle = len(password) // 2
    return password[middle:] + password[:middle]


def encrypt(password: str) -> str:
    """
    Encrypt a password string using upper_encryption() and swap_encryption()
    """
    return swap_encryption(upper_encryption(password))


def invalid_characters(username: str) -> list:
    """
    Check if username contains any invalid characters.
    All invalid charactes are stored in the list INVALID_CHARACTERS.
    Return the list of all invalid characters which are in username.
    The list can contain multiple instances of the same character.
    Return an empty list if no invalid characters are present in username.

    Examples
    ------------
    1)
    function input:
        username = "my_user@name!"

    function output:
        ['@', '!']

    2)
    function input:
        username = "?is_this_a(valid)_.username.

    function output.
        ['?', '(', ')', '.', '.']
    """
    return [char for char in INVALID_CHARACTERS if char in username]


def add_to_list(password: str, occ_password_list: list) -> None:
    """
    Add a unique password to occ_password_list.
    occ_password_list is a "list of lists" and has the format:

    [password_list, password_list, password_list, ...]

    Where password_list is a list containing two items:

    [number_of_password_occurences, password]

    number_of_password_occurences (int)     - counts how many times password has been used
    password (str)                          - a password string

    If the password cannot be found in any password_list,
    then append the occ_password_list with a new password_list with the format:

    [1, password]

    If the password is found in a password_list,
    then increment the number_of_password_occurences in the password_list containing the password.


    Examples
    ------------
    1)
    function input:
        password = "password"
        occ_password_list = [[2, "password"], [1, "second_password"]]

    occ_password_list after function completes:
        occ_password_list = [[3, "password"], [1, "second_password"]]

    2)
    function input:
        password = "unique_password"
        occ_password_list = [[2, "password"], [1, "second_password"]]

    occ_password_list after function completes:
        occ_password_list = [[2, "password"], [1, "second_password"], [1, unique_password]]

    """
    for list_password in occ_password_list:
        if password == list_password[1]:
            list_password[0] += 1
            return

    occ_password_list.append([1, password])


def add_multiple_passwords(passwords: str) -> list:
    """
    Given a string of passwords, return a list of list containing unique passwords
    and the occurences of a password.
    See function add_to_list() for the format of this list.

    The list should be created here, but all operations performed on the list
    should be done in add_to_list().

    Examples
    ------------
    1)
    function input:
        passwords = "password\n
                     password1\n
                     password\n
                     random_password"

    function output:
        [[2, password], [1, password1], [1, random_password]]


    2)
    function input:
        passwords = "just_one_password\n
                     just_one_password\n
                     just_one_password"

    function output:
        [[3, just_one_password]]

    """
    occ_password_list = []
    for password in passwords.split():
        add_to_list(password, occ_password_list)

    return occ_password_list


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


def create_password_dict(csv_file: str) -> dict:
    """
    A csv file (comma separated value) with services, usernames and passwords
    needs to be converted into a dictionary format in order to access the items easily.
    The csv file contain multiple lines and where line looks like:

    service;username;password

    OR

    service;username;

    In the end, we want the function to return a dictionary with the following format:
    {service: (username, encrypted_password), ...}

    service, username and encrypted_passwords are all strings.

    The passwords in the csv file should be encrypted using the encrypt() function to
    "maximize" password security.
    Use generate_password() to generate a random password if a service and a username does not have a password

    Examples
    ------------
    1)
    function input:
        csv_file = "google;yabs;super_pass\n
                    steam;pwner1337;\n
                    twitter;just_small_talk;this_is_not_secure"

    function output:
        {"google": ("yabs", _passSsuper), "steam": ("pwner1337", osqf7bas6z9kptvm), "twitter": (just_small_talk, ot_secureRthis_is_n)}

    """
    line_list = csv_file.split()
    password_dict = {}
    for line in line_list:
        service, username, password = line.split(";")
        if len(password) == 0:
            password = generate_password()
        else:
            password = encrypt(password)

        password_dict[service] = (username, password)

    return password_dict


# Check if password is greater than 6 and less than 66 characters.
# Also check if last character
def check_password_length(password):
    return True if 6 <= len(password) <= 80 else False


if __name__ == "__main__":
    print(encrypt("this_is_not_secure"))
    print(generate_password())
    print(
        create_password_dict(
            "google;yabs;super_pass\nsteam;pwner1337;\ntwitter;just_small_talk;this_is_not_secure"
        )
    )
