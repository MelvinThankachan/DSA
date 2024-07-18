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

    class AVLNode:
        def __init__(self, value):
            self.value = value
            self.left_child = None
            self.right_child = None
            self.height = 0

        def __str__(self):
            return f"Value: {self.value}"

    def height(self, node):
        return -1 if node is None else node.height
    
    def balance_factor(self, node):
        left_height = self.height(node.left_child)
        right_height = self.height(node.right_child)
        difference = left_height - right_height
        return difference

    def insert(self, value):

        def insertion(root):
            if root is None:
                return self.AVLNode(value)
            if value < root.value:
                root.left_child = insertion(root.left_child)
            else:
                root.right_child = insertion(root.right_child)

            left_height = self.height(root.left_child)
            right_heigth =self.height(root.right_child)
            root.height = max(left_height, right_heigth) + 1
            balance_factor = self.balance_factor(root)
            if balance_factor > 1:
                print(f"{root} is left heavy")
            elif balance_factor < -1:
                print(f"{root} is right heavy")
            return root

        self.root = insertion(self.root)


tree = AVLTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(9)
tree.insert(1)
print(tree.root.value)
print(tree.balance_factor(tree.root))