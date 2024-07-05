from queue import Queue


# 1. Reversing a queue
def reversing_queue(queue):
    elements = []
    while not queue.empty():
        elements.append(queue.get())
    length = len(elements)
    for i in range(length):
        queue.put(elements.pop())


# Testing
# queue = Queue()
# queue.put(30)
# queue.put(3800)
# queue.put(28)
# queue.put(8)
# print(list(queue.queue))
# reversing_queue(queue)
# print(list(queue.queue))


# 2. Building queue from an array
def array_to_queue(array):
    queue = Queue()
    for item in array:
        queue.put(item)
    return queue

array = [10, 40, 2, 46, 477]
result = array_to_queue(array)
print(list(result.queue))