# Heap
# insert(value)
# remove_root ()


class BinaryHeap:
    def __init__(self):
        self.heap = []
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def parent_index(self, child_index):
        return (child_index - 1) // 2

    def left_child_index(self, parent_index):
        return parent_index * 2 + 1

    def right_child_index(self, parent_index):
        return parent_index * 2 + 2

    def bubble_up(self, child_index):
        parent_index = self.parent_index(child_index)
        while parent_index >= 0:
            if self.heap[child_index] > self.heap[parent_index]:
                self.swap(child_index, parent_index)
            child_index = parent_index
            parent_index = self.parent_index(child_index)

    def bubble_down(self, parent_index):
        left_child_index = self.left_child_index(parent_index)
        right_child_index = self.right_child_index(parent_index)
        length = self.length
        while left_child_index < length and right_child_index < length:
            if self.heap[parent_index] < self.heap[left_child_index]:
                self.swap(parent_index, left_child_index)
                parent_index = left_child_index
            elif self.heap[parent_index] < self.heap[right_child_index]:
                self.swap(parent_index, right_child_index)
                parent_index = right_child_index
            left_child_index = self.left_child_index(parent_index)
            right_child_index = self.right_child_index(parent_index)

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        index = self.length - 1
        self.bubble_up(index)

    def remove_root(self):
        if self.is_empty():
            raise ValueError("Heap is empty")
        self.heap[0] = self.heap.pop()
        self.length -= 1
        parent_index = 0
        self.bubble_down(parent_index)

    def print_heap(self):
        print(self.heap)


# heap = BinaryHeap()
# heap.insert(10)
# heap.print_heap()
# heap.insert(20)
# heap.print_heap()
# heap.insert(30)
# heap.insert(40)
# heap.insert(50)
# heap.insert(60)
# heap.insert(70)
# heap.insert(80)
# heap.insert(90)
# heap.insert(90)
# heap.insert(100)
# heap.insert(100)
# heap.insert(80)
# heap.print_heap()
# heap.remove_root()
# heap.print_heap()
