#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    i = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndError:
            break
        else:
            count += 1
    print()
    return count
