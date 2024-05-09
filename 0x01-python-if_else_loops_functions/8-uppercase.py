#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' i<= char <= 'z':
            print("{}".format(chr(ord(char) - ord('a') + ord('A'))), end='')
