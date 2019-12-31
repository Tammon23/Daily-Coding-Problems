"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

import pickle
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    return pickle.dumps(root)

def deserialize(root):
    return pickle.loads(root)

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'


# nifty inefficient functions
# def serialize(root): # converts tree into XML structure
#     if root.left == None and root.right == None: # no nodes
#         return ("<Node>{}</Node>".format(root.val))
#
#     if root.left != None and root.right == None: # only left node
#         return ("<Node><Val>{}</Val><Left>{}</Left></Node>".format(root.val, serialize(root.left)))
#
#     if root.left == None and root.right != None: # only right node
#         return ("<Node><Val>{}</Val><Left>{}</Left></Node>".format(root.val, serialize(root.right)))
#
#     # 2 nodes
#     return ("<Node><Val>{}</Val><Left>{}</Left><Right>{}</Right></Node>".format(root.val, serialize(root.left), serialize(root.right)))

# def wrapper(root): # converts tree into dictionary structure
#     if root.left == None and root.right == None: # no nodes
#         return {'Val':root.val}
#
#     if root.left != None and root.right == None: # only left node
#         return {'Val':root.val, 'Left': serialize(root.left)}
#
#     if root.left == None and root.right != None: # only right node
#         return {'Val':root.val, 'Right': serialize(root.right)}
#
#     # 2 nodes
#     return {'Val':root.val, 'Left': serialize(root.left), 'Right':serialize(root.right)}
#
# def serialize(root): # used to convert dictionary into a string
#     return(repr(wrapper(root)))

























