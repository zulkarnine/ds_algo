from ds2 import Queue
from BinaryTreePrinter import BinaryTreePrinter

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            nodes = Queue()
            nodes.enqueue(self.root)

            while True:
                check_node = nodes.deque()
                if check_node.left is None:
                    check_node.left = TreeNode(val)
                    return
                elif check_node.right is None:
                    check_node.right = TreeNode(val)
                    return
                else:
                    nodes.enqueue(check_node.left)
                    nodes.enqueue(check_node.right)

    def __str__(self):
        tree_printer = BinaryTreePrinter()
        # tree_printer = BinaryTreePrinter(branch_line="_", extra_padding=0)
        return tree_printer.get_tree_string(self.root)


my_tree = BinaryTree()
for i in [1, 2, 3, 6, 7, 12, 45, 54, 12, 45, 76, 33, 12, 11, 101]:
    my_tree.insert(i)
    print(my_tree)
