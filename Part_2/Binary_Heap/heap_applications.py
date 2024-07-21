from binary_heap import BinaryHeap


# Heap sort
def heap_sort(array):
    heap = BinaryHeap()
    for value in array:
        heap.insert(value)
    for i in range(len(array) - 1, -1, -1):
        array[i] = heap.remove_root()
    return array


# array = [10, 654, 83, 1, 547, 38]
# print(heap_sort(array))


# Heap as a Priority Queue
class PriorityQueue:
    def __init__(self):
        self.heap = BinaryHeap()

    def enqueue(self, value):
        self.heap.insert(value)

    def dequeue(self):
        return self.heap.remove_root()

    def is_empty(self):
        return self.heap.is_empty()


# queue = PriorityQueue()
# queue.enqueue(30)
# queue.enqueue(40)
# queue.enqueue(10)
# queue.enqueue(60)
# print(queue.dequeue())
# print(queue.heap.heap)
