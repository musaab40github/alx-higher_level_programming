#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for i in my_list:
        add += my_list[i]
        if my_list[i] == my_list:
            continue
        i++
    return add
