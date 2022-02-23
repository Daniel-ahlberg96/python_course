# TODO
# yield, generators and decorators

# Conditonal statement


def conditional_statement(x: int):
    if x <= 0:
        print(f"{x} is not positive! BAD")

    elif x // 2 != (x + 1) // 2:
        print(f"{x} is an uneven number")
    
    else:
        print(f"{x} is an even number")

###############################################################################
# Iteration
def character_in_password_(password: str) -> bool:    
    for letter in password:
        if letter == "Ö":
            return True
    
    return False

# In operator
def password_in_password(password: str) -> bool:
    "password" in password

    return True if "password" in password else False # Iterate through string

###############################################################################
# Lists and tuples
def lists():
    numbers_and_vegetables = [0, 1, 2, "apelsin", "äpple", "gurka"] # Type invariant

    ls = [1, 2, 3, 4, 5] # 'list' is a reserved keyword
    ls[-1] = "Slut på nummer"
    ls[-2:]
    list("foooood")

    new_list = []
    for number in ls:
        new_number = number * 10
        new_list.append(new_number)
    
    
    new_list = [number * 10 for number in ls] # List comprehension
    print(new_list)

def tuples():
    allowed_vegetables = (1, 2, 3, 4, 5)
    allowed_vegetables[-1] = "slut på nummer"
    allowed_vegetables.append(6)

def useful_list_functions():
    vegetables_list = ["appelsin", "äpple", "tomat"]
    
    vegetables_string = ""
    for vegetable in vegetables_list:
        vegetables_string += vegetable + " "
    
    print(vegetables_string)
    
    vegetables_string = " ".join(vegetables_list)
    print(vegetables_string)

    vegetables_list = vegetables_string.split()
    print(vegetables_list)
    
###############################################################################
# Sets and dictionaries
def dictionaries():
    name_to_food = {"daniel": "max"} # Key and value
    name_to_food["daniel"]
    name_to_food["namn"] = "mat"
    # name_to_food["max"] # Error

    "daniel" in name_to_food

    # Show speed test

    for key in name_to_food:
        name_to_food[key] += " " + name_to_food[key]

    print(name_to_food)

    # Optional, if time
    for key, value in name_to_food.items():
        print(key, value)



if __name__ == "__main__":
    password = "this password is safe"
    print(password_in_password(password))
    useful_list_functions()
    dictionaries()
