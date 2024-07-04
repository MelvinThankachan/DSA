# Implementation of queue using list
class Queue:
    def __init__(self):
        self.queue = []
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def enqueue(self, item):
        self.queue.append(item)
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        dequeue_item = self.queue.pop(0)
        self.length -= 1
        return dequeue_item

    def peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.queue[0]


# Implementation of queue using linked list
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class QueueLL:
    def __init__(self, limit):
        self.head = None
        self.tail = None
        self.length = 0
        self.limit = limit

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.limit == self.length

    def enqueue(self, item):
        if self.is_full():
            raise ValueError("Queue is full")
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        dequeue_item = self.head
        self.head = dequeue_item.next
        self.length -= 1
        return dequeue_item.data

    def peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.head.data

    def print_queue(self):
        current_node = self.head
        print("[", end="")
        while current_node is not None:
            if current_node.next is not None:
                print(f"{current_node.data}, ", end="")
            else:
                print(f"{current_node.data}", end="")
            current_node = current_node.next
        print("]")


queue = QueueLL(5)
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(3)
queue.enqueue(20)
print(queue.peek())
queue.print_queue()