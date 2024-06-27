class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, key, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == key:
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                new_node.prev = current
                break
            current = current.next

    def insert_before(self, key, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == key:
                new_node.prev = current.prev
                if current.prev:
                    current.prev.next = new_node
                current.prev = new_node
                new_node.next = current
                if current == self.head:
                    self.head = new_node
                break
            current = current.next

    def delete(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                break
            current = current.next

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("End")

    def print_backward(self):
        current = self.head
        if current is None:
            return
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("Head")


dllist = DoublyLinkedList()


dllist.append(1)
dllist.append(2)
dllist.append(3)


print("Forward:", end=" ")
dllist.print_forward()
print("Backward:", end=" ")
dllist.print_backward()


dllist.insert_after(2, 4)
dllist.insert_before(3, 5)

print("Forward:", end=" ")
dllist.print_forward()


dllist.delete(4)

print("Forward:", end=" ")
dllist.print_forward()
