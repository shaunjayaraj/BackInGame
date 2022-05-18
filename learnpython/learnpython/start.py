#! /Users/shaunjayaraj/.pyenv/shims/python

from re import A
import sys

def hello(name):
    if name == 'Alice' or name == 'Andy':
        print('who the f* is ', name)
    else:
        print('reached the else case')

    name = name + '!!!'
    print('Hello', name)
    print('slice name[2:4] starts at index 2 and upto but not including 4', name[2:4])

def dictionaries():
    a = {}
    a['1'] = 'a'
    a['2'] = 'b'
    c = 'c'
    a[c] = c
    print("********************  Dictionaries  ************")
    print(a[c])
    if (a.get('peekachoo') == None):
        print("Did not find Peekachoo")
    if("peekachoo" not in a):
        print("Did not find Peekachoo in the Dict")
    if ("1" in a):
        print("Found the key 1")
    if ("a" in a):
        print("Found the value 1 ---> This does not work")
    all_keys = a.keys()
    print(all_keys)

    all_values = a.values()
    print(all_values)

    for k in sorted(a.keys()): print("key: {} -> {}".format(k, a[k]))

    all_items = a.items()

    print(all_items)

def py_cat(filename):
    print("*********** File Manipulations **********")
    f = open(filename,'r')
   # for line in f:
   #     print(line, end='')
 #   all_lines = f.readlines()
    all_lines_in_one_string = f.read()
    print(all_lines_in_one_string)
    f.close()

def peekabook():
    print('hello world')
    print(sys.argv)
    hello(sys.argv[1])
    dictionaries()
    py_cat(sys.argv[1])


if __name__ == '__main__':
    peekabook()
