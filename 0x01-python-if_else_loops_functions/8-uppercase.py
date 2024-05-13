#!/usr/bin/python3

def uppercase(str):
    result = ''
    for char in str:
        if 'a' <= char <= 'z':
            char_code = ord(char) - 32
            result += chr(char_code)
        else:
            result += char
    print("{}".format(result))
