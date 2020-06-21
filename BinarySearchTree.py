from BinaryTreePrinter import BinaryTreePrinter


class Node:
    def __init__(self, val):
        self.left: Node = None
        self.right: Node = None
        self.val = val


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.__insert(self.root, val)

    def __insert(self, node: Node, val):
        if node.val == val:
            return
        elif val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self.__insert(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self.__insert(node.right, val)

    def in_order(self):
        self.__in_order(self.root)

    def __in_order(self, node: Node):
        if node is None:
            return
        self.__in_order(node.left)
        print(node.val)
        self.__in_order(node.right)


bst = BinarySearchTree()
for i in [8, 4, 12, 2, 6, 10, 16, 1, 5, 7, 100, 200, 150, 9, 15]:
    bst.insert(i)
# bst.in_order()
BinaryTreePrinter(extra_padding=2).print_node(bst.root)