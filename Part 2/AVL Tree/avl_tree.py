# My implementation
# class AVLTree:
#     def __init__(self):
#         self.root = None

#     class _AVLNode:
#         def __init__(self, value=None):
#             self.value = value
#             self.left_child = None
#             self.right_child = None

#         def __str__(self):
#             return f"Value: {self.value}"

#     def insert(self, value):
#         new_node = self._AVLNode(value)

#         def _insert(node):
#             if value < node.value:
#                 if node.left_child is None:
#                     node.left_child = new_node
#                     return
#                 else:
#                     _insert(node.left_child)
#             else:
#                 if node.right_child is None:
#                     node.right_child = new_node
#                     return
#                 else:
#                     _insert(node.right_child)

#         root = self.root
#         if root is None:
#             self.root = new_node
#             return
#         _insert(root)


class AVLTree:
    def __init__(self):
        self.root = None

    class _AVLNode:
        def __init__(self, value):
            self.value = value
            self.left_child = None
            self.right_child = None

        def __str__(self):
            return f"Value: {self.value}"

    def insert(self, value):

        def _insert(root):
            if root is None:
                return self._AVLNode(value)
            if value < root.value:
                root.left_child = _insert(root.left_child)
            else:
                root.right_child = _insert(root.right_child)
            return root

        self.root = _insert(self.root)


tree = AVLTree()
tree.insert(20)
tree.insert(30)
tree.insert(10)
tree.insert(5)
tree.insert(9)
print(tree.root.value)