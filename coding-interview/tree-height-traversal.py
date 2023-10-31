class Node:
    def __init__(self, left_child, right_child):
        self.left_child = left_child
        self.right_child = right_child

    def height(self):
        if (self.left_child is None) and (self.right_child is None):
            return 0

        current_left_child_height = 1 + \
            self.left_child.height() if self.left_child is not None else 0
        current_right_child_height = 1 + \
            self.right_child.height() if self.right_child is not None else 0

        return max(current_left_child_height, current_right_child_height)


if __name__ == '__main__':
    # leaf1 = Node(None, None)
    # leaf2 = Node(None, None)
    # node = Node(leaf1, None)
    # root = Node(node, leaf2)

    # print(f"Height of the tree: {root.height()}")

    # root = Node(None, None)
    # print(f"Height of the tree: {root.height()}")
