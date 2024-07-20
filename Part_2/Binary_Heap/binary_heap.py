class BinaryHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def parent_index(self, child_index):
        return (child_index - 1) // 2

    def left_index(self, parent_index):
        return parent_index * 2 + 1

    def right_index(self, parent_index):
        return parent_index * 2 + 2

    def has_left(self, parent_index):
        return self.left_index(parent_index) < self.size

    def has_right(self, parent_index):
        return self.right_index(parent_index) < self.size

    def largest_child_index(self, parent_index):
        left_index = self.left_index(parent_index)
        right_index = self.right_index(parent_index)
        if self.heap[left_index] >= self.heap[right_index]:
            return left_index
        return right_index

    def down_swap_index(self, parent_index):
        has_left = self.has_left(parent_index)
        has_right = self.has_right(parent_index)
        if has_left and has_right:
            return self.largest_child_index(parent_index)
        elif has_left:
            return self.left_index(parent_index)
        elif has_right:
            return self.right_index(parent_index)
        else:
            return parent_index

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def bubble_up(self, index):
        parent_index = self.parent_index(index)
        while parent_index >= 0:
            if self.heap[index] > self.heap[parent_index]:
                self.swap(index, parent_index)
                index = parent_index
                parent_index = self.parent_index(index)
            else:
                break

    def bubble_down(self, parent_index):
        parent_value = self.heap[parent_index]
        down_index = self.down_swap_index(parent_index)
        down_value = self.heap[down_index]
        if parent_value < down_value:
            self.swap(down_index, parent_index)
            self.bubble_down(down_index)

    def insert(self, value):
        self.heap.append(value)
        index = self.size
        self.size += 1
        self.bubble_up(index)

    def remove_root(self):
        if self.is_empty():
            raise ValueError("Heap is empty")
        if self.size == 1:
            self.size -= 1
            return self.heap.pop()

        root_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        root_index = 0
        self.bubble_down(root_index)
        return root_value


# heap = BinaryHeap()
# heap.insert(10)
# heap.insert(20)
# heap.insert(30)
# heap.insert(40)
# heap.insert(50)
# heap.insert(48)
# heap.insert(50)
# heap.remove_root()
# heap.remove_root()
# heap.remove_root()
# heap.remove_root()
# heap.remove_root()
# heap.remove_root()
# heap.insert(50)
# print(heap.heap)
