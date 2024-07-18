class BinarySearchTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.left_child = None
            self.right_child = None

    def insert(self, value):
        def insertion(root):
            if root is None:
                return self.Node(value)
            if value == root.value:
                raise ValueError("Value already exists")
            elif value > root.value:
                root.right_child = insertion(root.right_child)
            elif value < root.value:
                root.left_child = insertion(root.left_child)
            return root

        self.root = insertion(self.root)

    def find(self, value):
        def finding(root):
            if root is None:
                return False
            if value == root.value:
                return root
            elif value > root.value:
                return finding(root.right_child)
            elif value < root.value:
                return finding(root.left_child)

        return finding(self.root)

    def pre_order(self):
        values = []

        def traverse(root):
            if root is None:
                return
            values.append(root.value)
            traverse(root.left_child)
            traverse(root.right_child)

        traverse(self.root)
        return values

    def in_order(self):
        values = []

        def traverse(root):
            if root is None:
                return
            traverse(root.left_child)
            values.append(root.value)
            traverse(root.right_child)

        traverse(self.root)
        return values

    def post_order(self):
        values = []

        def traverse(root):
            if root is None:
                return
            traverse(root.left_child)
            traverse(root.right_child)
            values.append(root.value)

        traverse(self.root)
        return values

    def delete(self, value):
        def find_max(root):
            while root.right_child is not None:
                root = root.right_child
            return root.value

        def deletion(root, value):
            if root is None:
                raise ValueError("Value not found")
            if value < root.value:
                root.left_child = deletion(root.left_child, value)
            elif value > root.value:
                root.right_child = deletion(root.right_child, value)
            else:
                # Deleting if the node have zero or one child
                if root.left_child is None:
                    return root.right_child
                elif root.right_child is None:
                    return root.left_child

                # Deleting if the node have two childs
                max_value = find_max(root.left_child)
                root.value = max_value
                deletion(root.left_child, max_value)

            return root

        root = self.root
        # Check if the root node itself has the target value
        if root is not None and root.value == value:
            if root.left_child is None:
                self.root = root.right_child
                del root
                return
            if root.right_child is None:
                self.root = root.left_child
                del root
                return
        deletion(root, value)
    
    def count(self):
        def counting(root):
            if root is None:
                return 0
            left_count = counting(root.left_child)
            right_count = counting(root.right_child)
            return 1 + left_count + right_count
        return counting(self.root)


tree = BinarySearchTree()
values = []
for value in values:
    tree.insert(value)
print(tree.find(6))
# for value in values[:-1]:
#     tree.delete(value)
tree.delete(10)
print(tree.pre_order())
print(tree.in_order())
print(tree.post_order())
print(tree.count())