import Tree


def equal(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.value != root2.value:
        return False
    
    return equal(root1.left_child, root2.left_child)





tree1 = Tree()
tree1.insert(7)
tree1.insert(4)
tree1.insert(9)
tree1.insert(1)
tree1.insert(6)
tree1.insert(8)
tree1.insert(10)
tree2 = Tree()
tree2.insert(7)
tree2.insert(4)
tree2.insert(9)
tree2.insert(1)
tree2.insert(6)
tree2.insert(8)
tree2.insert(10)

print(equal(tree1.root, tree2.root))