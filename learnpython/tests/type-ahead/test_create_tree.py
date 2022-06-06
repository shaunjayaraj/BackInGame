import os
import sys
import os

sys.path.append(os.path.abspath('./learnpython/type-ahead'))
print(sys.path)

import  create_tree
import node


def test_add_words_with_same_first_letter_into_tree():
    input_list = ['a',  'an', 'are', 'art', 'array']
    root_node = create_tree.add_list_to_tree(input_list)
    first_level_child_list = root_node.get_children()
    assert len(first_level_child_list) == 4
    assert root_node.to_string() == "Value: a : n re rt rray"

''' are art should give me a -> re rt ->  e  t'''
def test_recursively_add_words_till_all_leaf_nodes_are_len_1():
    input_list = ['are', 'art']
    root_node = create_tree.add_list_to_tree(input_list)
    first_level_child_list = root_node.get_children()
    assert len(first_level_child_list) == 2

    assert first_level_child_list[0].to_string() == "Value: re : e"
    assert first_level_child_list[1].to_string() == "Value: rt : t"
