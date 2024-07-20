from tree import Tree


def pre_order_traversal(root):  # Root -> Left SubTree -> Right SubTree
    if root is None:
        return
    print(root.value, end=" - ")
    pre_order_traversal(root.left_child)
    pre_order_traversal(root.right_child)


def in_order_traversal(root):  # Left SubTree -> Root -> Right SubTree
    if root is None:
        return
    in_order_traversal(root.left_child)
    print(root.value, end=" - ")
    in_order_traversal(root.right_child)


def post_order_traversal(root):  # Left SubTree -> Right SubTree -> Root
    if root is None:
        return
    post_order_traversal(root.left_child)
    post_order_traversal(root.right_child)
    print(root.value, end=" - ")





tree = Tree()
tree.insert(7)
tree.insert(4)
tree.insert(9)
tree.insert(1)
tree.insert(6)
tree.insert(8)
tree.insert(10)
pre_order_traversal(tree.root)
print()
in_order_traversal(tree.root)
print()
post_order_traversal(tree.root)
print()