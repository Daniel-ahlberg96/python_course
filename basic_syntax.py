# TODO
# Dictionaries, tuples and sets

# Basic syntax, loops, conditional statements and strings
# Content:
# - print() and string formatting
#   getting_started()
#
# - String manipulaiton, indexing and operators
#   upper_encryption(), swap_encryptions() 

# print: Welcome user: "<user>". You are using version <version_nr> of this program!
def getting_started(user, version_nr):
    print(f'Welcome user "{user}". You are using version {version_nr} of this program!')

# Add the capitalized second to last character to the password    
def upper_encryption(password):
    return password + password[-2].upper()

# Swap the first and second half of the password
def swap_encryption(password):
    middle = len(password)//2
    return password[middle:] + password[:middle] 

# Encrypt a password string
def encrypt(password):
    return swap_encryption(upper_encryption(password))

# Add a unique password to a list of passwords 
def add_to_list(password, encrypted_password_list):
    encrypted_password = encrypt(password)
    for list_password in encrypted_password_list:
        if encrypted_password == list_password[1]:
            list_password[0] += 1
            return
    
    encrypted_password_list.append([1, encrypted_password])
    
# Encrypt a string a passwords separated by a newline
def encrypt_multiple_passwords(passwords, encrypted_password_list):
    for password in passwords.split():
        add_to_list(password, encrypted_password_list)

# Check if password is greater than 6 and less than 66 characters.
# Also check if last character 
def check_password_length(password):
    return True if 6 <= len(password) <= 80 else False

def invalid_characters_comprehension(username, invalid_character_list):
    return [char for char in invalid_character_list if char in username]

def invalid_characters_in(username, invalid_character_list):
    return_list = []
    for char in invalid_character_list:
        if char in username:
            return_list.append(char)
    return return_list
    

def invalid_characters_set(username, character_set):
    return [char for char in username if char in character_set]

if __name__ == "__main__":
    print(encrypt("password"))
    
