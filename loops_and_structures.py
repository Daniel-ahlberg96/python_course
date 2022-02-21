# TODO
# Hash tables and sets

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

    list("foooood")
    ls = [1, 2, 3, 4, 5] # 'list' is a reserved keyword
    ls[-1] = "Slut på nummer"
    ls[-2:]

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
    


if __name__ == "__main__":
    password = "this password is safe"
    print(password_in_password(password))
    useful_list_functions()
