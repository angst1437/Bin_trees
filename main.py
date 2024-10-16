from random import randint
import time
from tree_class import Tree
from node_class import Node

tree = Tree()

tree.add_vertex(10)
tree.add_vertex(15)
tree.add_vertex(5)
tree.add_vertex(7)
tree.add_vertex(12)
tree.add_vertex(17)

tree.delete_value(15)
print(tree.find_key(15))

print(tree.keylist)