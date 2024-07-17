# My implementation of binary search tree

# class Node:
#     def __init__(self, val=None, left_child=None, right_child=None):
#         self.val = val
#         self.left_child = left_child
#         self.right_child = right_child


# class Tree:
#     def __init__(self):
#         self.root = None

#     def is_empty(self):
#         return self.root is None

#     def near_node(self, target, node=None):
#         if node is None:
#             node = self.root
#         if self.is_empty():
#             return False
#         if target < node.val:
#             if node.left_child is None:
#                 return node
#             else:
#                 return self.near_node(target, node=node.left_child)
#         elif target > node.val:
#             if node.right_child is None:
#                 return node
#             else:
#                 return self.near_node(target, node=node.right_child)
#         elif target == node.val:
#             return False

#     def insert(self, val):
#         new_node = Node(val=val)
#         if self.is_empty():
#             self.root = new_node
#             return
#         near_node = self.near_node(val, node=self.root)
#         if not near_node:
#             raise ValueError("Value already exists")
#         if val > near_node.val:
#             near_node.right_child = new_node
#         elif val < near_node.val:
#             near_node.left_child = new_node

#     def find(self, val):
#         if self.is_empty():
#             return False
#         not_exist = self.near_node(target=val, node=self.root)
#         if not_exist:
#             return False
#         else:
#             return True


# tree = Tree()
# tree.insert(10)
# tree.insert(5)
# tree.insert(15)
# print(tree.find(10))


class Tree:
    def __init__(self):
        self.root = None

    class _Node:
        def __init__(self, value=None):
            self.value = value
            self.left_child = None
            self.right_child = None

        def __str__(self) -> str:
            return f"Node Value - {self.value}"

    def is_empty(self):
        return self.root is None

    def insert(self, value):
        new_node = self._Node(value)
        if self.is_empty():
            self.root = new_node
            return True

        current = self.root
        while True:
            current_value = current.value
            if value > current_value:
                if current.right_child is None:
                    current.right_child = new_node
                    break
                current = current.right_child
            elif value < current_value:
                if current.left_child is None:
                    current.left_child = new_node
                    break
                current = current.left_child

    def find(self, value):
        current = self.root
        while current is not None:
            current_value = current.value
            if value == current_value:
                return True
            elif value > current_value:
                current = current.right_child
            elif value < current_value:
                current = current.left_child
        return False

    def is_leaf(self, node):
        return node.left_child is None and node.right_child is None

    # Using post order traversal
    def height(self):
        def _height(root):
            if root is None:
                return -1
            if self.is_leaf(root):
                return 0
            left_height = _height(root.left_child)
            right_height = _height(root.right_child)
            return 1 + max(left_height, right_height)

        root = self.root
        return _height(root)

    def minimum(self):
        def _minimum(root):
            if root is None:
                return float("inf")
            if self.is_leaf(root):
                return root.value
            left_min = _minimum(root.left_child)
            right_min = _minimum(root.right_child)
            min_value = min(left_min, right_min, root.value)
            return min_value

        root = self.root
        if root is None:
            raise ValueError("Tree is empty")
        return _minimum(root)

    def equals(self, other_tree):
        def _equals(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            left = _equals(root1.left_child, root2.left_child)
            right = _equals(root1.right_child, root2.right_child)
            return root1.value == root2.value and left and right

        tree1_root = self.root
        tree2_root = other_tree.root
        if tree1.root is None and tree2.root is None:
            return True
        if tree1.root is None or tree2.root is None:
            raise ValueError("Empty Tree")
        return _equals(tree1_root, tree2_root)

    def is_bst(self):
        def _validate(root, low, high):
            if root is None:
                return True
            value = root.value
            if value < low or value > high:
                return False
            left = _validate(root.left_child, low, value - 1)
            right = _validate(root.right_child, value + 1, high)
            return left and right

        root = self.root
        low = float("-inf")
        high = float("inf")
        return _validate(root, low, high)
    
    
    def print_values_at_distance(self, k):
        values = []
        def _values_at_distance(root, k):
            if root is None:
                return
            if k == 0:
                values.append(root.value)
                return
            _values_at_distance(root.left_child, k - 1)
            _values_at_distance(root.right_child, k - 1)
        
        root = self.root
        _values_at_distance(root, k)
        return values

    # For Testing
    # def swaproot(self):
    #     root = self.root
    #     root.left_child , root.right_child = root.right_child, root.left_child


# Tree 1
tree1 = Tree()
tree1.insert(7)
tree1.insert(4)
tree1.insert(9)
tree1.insert(1)
tree1.insert(6)
tree1.insert(8)
tree1.insert(10)
tree1.insert(-1)

# Tree 2
tree2 = Tree()
tree2.insert(7)
tree2.insert(4)
tree2.insert(9)
tree2.insert(1)
tree2.insert(6)
tree2.insert(8)
tree2.insert(10)

print(tree1.print_values_at_distance(0))
print(tree1.print_values_at_distance(1))
print(tree1.print_values_at_distance(2))
print(tree1.print_values_at_distance(3))
