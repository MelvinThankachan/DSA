from binary_heap import BinaryHeap


values = [10, 654, 83, 1, 547, 38]
heap = BinaryHeap()
for value in values:
    heap.insert(value)


for i in range(len(values) - 1, -1 , -1):
    values[i] = heap.remove_root()

print(values)