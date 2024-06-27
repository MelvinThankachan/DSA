class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("End")

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, value):
        if not self.head:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def insert_after(self, value, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def insert_before(self, value, data):
        new_node = Node(data)
        if not self.head:
            return

        if self.head.data == value:
            new_node.next = self.head
            self.head = new_node
            return

        prev = None
        current = self.head
        while current:
            if current.data == value:
                new_node.next = current
                prev.next = new_node
                return
            prev = current
            current = current.next


sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.print_list()

sll.prepend(0)
sll.print_list()

sll.delete_node(2)
sll.print_list()

sll.insert_after(1, 2.5)
sll.print_list()

sll.insert_before(3, 2.7)
sll.print_list()
