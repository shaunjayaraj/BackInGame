#! /Users/shaunjayaraj/.pyenv/shims/python

import node

def add_keyValue_to_dict(dict, word):
    if(dict.get(word[0])):
        list = dict.get(word[0])
        list.append(word)
    else:
        list = []
        list.append(word)
        dict[word[0]] = list

def add_word_to_dict(line, dict):
    for word in line.split():
        print(word)
        add_keyValue_to_dict(dict, word)
    return dict


def get_second_part_or_empty(str):
    if len(str) > 1:
        return str[1:]
    else:
        return ""

def add_list_to_tree(list):
    first_value = list[0]
    root_char = first_value[0]
    root_node = node.Node(root_char)

    list_child_words = []
    for word in list:
        child_word = get_second_part_or_empty(word)
        if(len(child_word) > 0):
            list_child_words.append(child_word)  

    if(len(list_child_words) > 0):
          return_node  = add_list_to_tree(list_child_words)
          root_node.add_child(node.Node(return_node))

    return root_node


