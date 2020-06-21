"""
Printer Utility to print a binary tree like a tree.

Can print a binary tree whose root node has at least the following properties.

node.left    # left child
node.right   # right child
node.val     # value of the node
"""


class NodePrintData:
    def __init__(self, lines: list, root_position, root_len):
        self.lines = lines
        self.root_position = root_position
        self.root_len = root_len
        self.max_width = 0 if len(lines) == 0 else max([len(line) for line in self.lines])
        self.height = len(self.lines)


class BinaryTreePrinter:
    def __init__(self, branch_line=".", left_node_line="/", right_node_line="\\", extra_padding=1):
        self.branch_line = branch_line
        self.left_node_line = left_node_line
        self.right_node_line = right_node_line
        self.extra_padding = extra_padding

    def __treeify(self, node):
        if node is None:
            return NodePrintData([], 0, 0)

        val = f"{node.val}"
        left_node_data = self.__treeify(node.left)
        right_node_data = self.__treeify(node.right)
        lines = []
        first_line = ""
        second_line = ""
        len_before_val = 0
        if left_node_data.max_width > 0:
            left_root_end = left_node_data.root_len + left_node_data.root_position
            branch_len = left_node_data.max_width - (left_node_data.root_position + left_node_data.root_len)
            first_line += " " * (left_root_end + 1)
            first_line += self.branch_line * (branch_len + self.extra_padding)
            len_before_val = len(first_line)
            second_line += " " * left_root_end + self.left_node_line
            second_line += " " * (len_before_val - len(second_line))

        first_line += val
        left_padding = "" if right_node_data.max_width == 0 else " " * (len(val) + 1 + self.extra_padding)
        if right_node_data.max_width > 0:
            first_line += self.branch_line * (right_node_data.root_position + self.extra_padding)
            second_line += " " * (right_node_data.root_position + len(val) + self.extra_padding) + self.right_node_line

        lines.append(first_line)
        lines.append(second_line)
        for i in range(max(left_node_data.height, right_node_data.height)):
            if i < left_node_data.height and i < right_node_data.height:
                left_line: str = left_node_data.lines[i]
                right_line: str = right_node_data.lines[i]
            elif i < left_node_data.height:
                left_line = left_node_data.lines[i]
                right_line = ""
            else:
                right_line = right_node_data.lines[i]
                left_line = ""
            lines.append(
                "{:<{l_width}}{}{:<{r_width}}".format(left_line, left_padding, right_line, l_width=len_before_val,
                                                      r_width=right_node_data.max_width))
        return NodePrintData(lines, len_before_val, len(val))

    def print_node(self, root_node):
        node_data = self.__treeify(root_node)
        for line in node_data.lines:
            print(line)

    def get_tree_string(self, root_node):
        node_data = self.__treeify(root_node)
        return "\n".join(node_data.lines)
