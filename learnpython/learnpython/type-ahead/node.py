from multiprocessing.sharedctypes import Value


class Node():

    value = ''
    children = []

    def __init__(self, node_value) -> None:
        self.value = node_value

    def add_child(self, node):
        self.children.append(node)
    
    def get_value(self):
        return self.value

    def get_children(self):
        return self.children
    
    def to_string(self):
        str = "Value: " + self.value + " :"
        for child in self.children:
            str = str + " " + child.get_value()
        return str
