# TODO
# Create another test with lists, multiple types? Split? Pass by reference

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
 
# Check if password is greater than 6 and less than 66 characters.
# Also check if last character 
def check_password_length(password):
    return True if 6 <= len(password) <= 80 else False

def invalid_characters_nested(username, invalid_character_list):
    return_list = []
    for char in invalid_character_list:
        for letter in username:
            if char == letter:
                return_list.append(char)

    return return_list

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
    getting_started("dsad", 1)
    
