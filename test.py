import timeit
from basic_syntax import *

def invalid_characters_nested(username, invalid_character_list):
    return_list = []
    for char in invalid_character_list:
        for letter in username:
            if char == letter:
                return_list.append(char)

    return return_list

def check_username_test():
    USERNAME = "python_is_great!"
    INVALID_CHARACTER_LIST = ["_", "!", "@", "\\", "?", "\"", "(", ")", "{", "}"]
    INVALID_CHARACTER_SET = set(INVALID_CHARACTER_LIST)

    t1 = timeit.timeit(lambda: invalid_characters_nested(USERNAME, INVALID_CHARACTER_LIST), number=100)
    t2 = timeit.timeit(lambda: invalid_characters_comprehension(USERNAME, INVALID_CHARACTER_LIST), number=100)
    t3 = timeit.timeit(lambda: invalid_characters_in(USERNAME, INVALID_CHARACTER_LIST), number=100)
    t4 = timeit.timeit(lambda: invalid_characters_set(USERNAME, INVALID_CHARACTER_SET), number=100)

    print(f"Nested: {t1}, Comprehension: {t2}, In: {t3}, Set: {t4}")

def in_operator(range):
    return 99999 in range
    
def check_in_operator():
    list_range = list(range(1,100000))
    set_range = set(range(1,100000))
    t1 = timeit.timeit(lambda: in_operator(list_range), number=100)
    t2 = timeit.timeit(lambda: in_operator(set_range), number=100)

    print(f"List: {t1}, Set: {t2}")

if __name__ == "__main__":
    check_username_test()
    check_in_operator()