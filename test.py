from cgi import test
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

def in_operator(range):
    return 99999 in range
    
def check_in_operator():
    list_range = list(range(1,100000))
    set_range = set(range(1,100000))
    t1 = timeit.timeit(lambda: in_operator(list_range), number=100)
    t2 = timeit.timeit(lambda: in_operator(set_range), number=100)

    print(f"List: {t1}, Set: {t2}")

def test_list():
    ls = [1,2,3,4]
    print(f"Within function: {id(ls)}")
    return ls

def test_dict():
    d = {}
    d[1] = 2
    d[3] = 4
    d[2] = 3
    d[0] = 1
    del d[2]
    for k in d:
        print(k)

if __name__ == "__main__":
    check_username_test()
    check_in_operator()
    ls = test_list()
    print(f"Outside function: {id(ls)}")
    test_dict()