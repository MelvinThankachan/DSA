class AVLTree:
    class AVLNode:
        def __init__(self, value):
            self.value = value
            self.left_child = None
            self.right_child = None
            self.height = 0

        def __str__(self):
            return f"Value: {self.value}"

    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node is not None else -1

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left_child) - self.height(node.right_child)

    def is_left_heavy(self, node):
        return self.balance_factor(node) > 1

    def is_right_heavy(self, node):
        return self.balance_factor(node) < -1

    def set_height(self, node):
        return max(self.height(node.left_child), self.height(node.right_child)) + 1

    def left_rotate(self, root):
        new_root = root.right_child
        root.right_child = new_root.left_child
        new_root.left_child = root
        root.height = self.set_height(root)
        new_root.height = self.set_height(new_root)
        return new_root

    def right_rotate(self, root):
        new_root = root.left_child
        root.left_child = new_root.right_child
        new_root.right_child = root
        root.height = self.set_height(root)
        new_root.height = self.set_height(new_root)
        return new_root

    def balance(self, root):
        if self.is_left_heavy(root):
            if self.balance_factor(root.left_child) < 0:
                root.left_child = self.left_rotate(root.left_child)
            root = self.right_rotate(root)
        elif self.is_right_heavy(root):
            if self.balance_factor(root.right_child) > 0:
                root.right_child = self.right_rotate(root.right_child)
            root = self.left_rotate(root)
        return root

    def insert(self, value):
        def insertion(root):
            if root is None:
                return self.AVLNode(value)
            if value < root.value:
                root.left_child = insertion(root.left_child)
            else:
                root.right_child = insertion(root.right_child)

            root.height = self.set_height(root)
            return self.balance(root)

        self.root = insertion(self.root)


tree = AVLTree()
tree.insert(10)
tree.insert(30)
tree.insert(20)
print(tree.root)
