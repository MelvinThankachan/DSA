# Implementation of queue using list
class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.length = 0
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front > self.rear
    
    def is_full(self):
        pass

    def enqueue(self, item):
        self.queue.append(item)
        self.length += 1
        self.rear += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        dequeue_item = self.queue[self.front]
        self.front += 1
        self.length -= 1
        return dequeue_item

    def peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.queue[self.front]


# Implementation of queue using linked list
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class QueueLL:
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.length = 0
        self.capacity = capacity

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.capacity == self.length

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


# Testing
# queue = Queue(5)
# queue.enqueue(5)
# queue.enqueue(10)
# queue.enqueue(3)
# queue.enqueue(20)
# print(queue.peek())
# queue.print_queue()


class PriorityQueue:
    def __init__(self) -> None:
        self.queue = 9

