import timeit

RANGE = 1000000
ran = range(RANGE)
RAN_LIST = list(ran)
RAN_DICT = dict.fromkeys(RAN_LIST, "True")

def list_index():
    (RANGE - 1) in RAN_LIST

def dict_index():
    (RANGE - 1) in RAN_DICT

t_find_in_list = timeit.timeit(lambda: list_index(), number=10)
t_find_in_dict = timeit.timeit(lambda: dict_index(), number=10)

print(f"Find in list: {t_find_in_list} s, Find in dict: {t_find_in_dict} s")



