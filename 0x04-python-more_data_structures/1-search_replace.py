#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for x in my_list:
        if my_list[x] == search:
            my_list[x].append(replace)
    return my_list