from queue import Queue

q = Queue(maxsize=5)

q.put(10, timeout=1)
q.put(20, timeout=1)
q.put(30, timeout=1)
q.put(40, timeout=1)
q.put(50, timeout=1)
q.get(timeout=1)


print(list(q.queue))