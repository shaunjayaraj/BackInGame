#! /Users/shaunjayaraj/.pyenv/shims/python

from re import A, sub
import sys
import re
import os
import shutil
import subprocess
import prime

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

def Find(pat, text):
    match = re.search(pat,text)
    if match:
        print(match.group())
    else:
        print("match not found")

def reg_ex():
    text = "called piiig"

    pat = "iig"
    match_object = re.search(pat, text)
    print(match_object.group())

    unsucceful_pat = "meek"
    match_object = re.search(unsucceful_pat, text)
    if match_object:
        print(match_object.group())
    else:
        print("Match not found")

    # . stands for any char
    Find("...g", text)

    Find("..gs", "called piig") #there is no s so will not find

    Find("x..g","called piiig much better: xyzg") #will find the second instance xyzg

    Find("x\.zg","called piiig much better: x.zg") #escape special character with a backslash

    Find(r":\w\w\w","123 :cat blah blah") #use r to not let the text editor mess with the string send it in raw, and \w means any alphanumeric including _

    Find(r"\d\d\d","123 :cat blah blah") #digits

    Find(r"\d\s\d\s\d","1 2 3 :cat blah blah") #\s matches white spaces

    Find(r"\d\s+\d\s+\d\s*\d","1 2       34 :cat blah blah") # + means one or more, * means 0 or more

    Find(r":\w+","1 2       34 :kitten blah blah") # 

    Find(r":\S+","1 2       34 :kittenflgk3o4f34_2342@£$@2397823   blah blah") # get : and all characters till you find the first non-whitespace character

    Find(r"[\w.]+@[\w.]+","1 2       34 :kitten a.bgh@gmail.com blah blah") #   
    print("************ Selecting groups *********")
    m = re.search(r"([\w.]+)@([\w.]+)","1 2       34 :kitten a.bgh@gmail.com blah blah")
    print(m.group())
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))

    list_of_matches = re.findall("[\w.]+@[\w.]+","1 2       34 :kitten a.bgh@gmail.com blah blah foo@bar.com") 
    print(list_of_matches)

    list_of_matches = re.findall("([\w.]+)@([\w.]+)","1 2       34 :kitten a.bgh@gmail.com blah blah foo@bar.com") # gives tuples
    print(list_of_matches)

def os_ops():
    print("************* OS ******************")
    filenames = os.listdir(".")
    print(filenames)
    print(os.path.join(".",filenames[0]))
    print(os.path.abspath(os.path.join(".",filenames[0])))
    print(os.path.exists("/tmp"))
    shutil.copy("./prime.py", "./prime_copy.py")

   # (status,output) = subprocess.getstatusoutput("*%$%$%ls -l")
   # if (status):
  #      print("{} there as an error: {} ".format(sys.stderr, output))
       # sys.stderr.write(output)
       # sys.exit(1)
  #ß  print(output)

def exceptions():
    try: 
        f = open("bboop.txt")
        text = f.read()
        print(text)
    except IOError:
        print("Did not file IO ERROR: boop.txt")

def modularity():
    print("*********** Modularity *********")
    print(dir(prime))

    print(sys.path)
    #import babynames
    #print(dir(babynames))

def urls():
    import urllib.request

    uf = urllib.request.urlopen("http://www.google.com")
    #print(uf.read())
    urllib.request.urlretrieve("https://www.google.com/logos/doodles/2022/gama-pehlwans-144th-birthday-6753651837109412-2x.png", "gama.png")

def sq(a):
    return a*a

def list_comprehension():
    print("********** Crazy closure shit in python**********")

    a = ['aaaaa', 'fff', 'rrrr']
    result = [len(s) for s in a]
    print(result)

    a = [4, 5, 7]
    result = [sq(s) for s in a if s > 4]
    print(result)


def has_r(str):
    print("£££££££££££££Entering HAS R function££££££££££££")
    found_r_flag = False
    for char in str:
        if(char == 'r'):
            print("Found R")
            found_r_flag = True
            break

    if found_r_flag == False:
        print("not found R")

def peekabook():
    print('hello world')
    print(sys.argv)
    hello(sys.argv[1])
    dictionaries()
    py_cat(sys.argv[1])
    reg_ex()
    os_ops()
    modularity()
    urls()
    list_comprehension()
    has_r("kjdfbrufbu")

    sys.path.append(os.path.abspath('./google-python-exercises/basic'))
    print(sys.path)

    import wordcount

    print(wordcount.__file__)
    print(wordcount.create_word_count_dictionary('./mergesort.py'))


if __name__ == '__main__':
    peekabook()
