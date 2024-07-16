from queue import Queue, PriorityQueue


# # 1. Reversing a queue
# def reversing_queue(queue):
#     elements = []
#     while not queue.empty():
#         elements.append(queue.get())
#     length = len(elements)
#     for i in range(length):
#         queue.put(elements.pop())

# def reversing_q_recur(queue):
#     if queue.empty():
#         return
#     item = queue.get()
#     reversing_q_recur(queue)
#     queue.put(item)


# # Testing
# queue = Queue()
# queue.put(30)
# queue.put(3800)
# queue.put(28)
# queue.put(8)
# print(list(queue.queue))
# reversing_q_recur(queue)
# print(list(queue.queue))


# # 2. Building queue from an array
# def array_to_queue(array):
#     queue = Queue()
#     for item in array:
#         queue.put(item)
#     return queue

# array = [10, 40, 2, 46, 477]
# result = array_to_queue(array)
# print(list(result.queue))


prio = PriorityQueue()
prio.put(("xata1000", 100))
prio.put(("data2", 20))
prio.put(("data3", 50))
prio.put(("data4", 3))

# Inserting a tuple with priority explicitly
prio.put(("melvin", 1))
prio.put((20, 1))
print(prio.get())
print(list(prio.queue))