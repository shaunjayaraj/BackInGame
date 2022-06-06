import os
import sys
import os

sys.path.append(os.path.abspath('./learnpython/type-ahead'))
print(sys.path)

import create_tree 
import node

def test_create_a_node_with_no_children():
    root = node.Node('a')
    assert root.get_value() == 'a'
    assert root.to_string() == "Value: a :"

def test_create_a_node_with_children():
    root = node.Node('a')
    root.add_child(node.Node('n'))
    root.add_child(node.Node('re'))
    root.add_child(node.Node('rt'))
    assert root.get_value() == 'a'

    assert root.to_string() == "Value: a : n re rt"