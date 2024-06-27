class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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

    def remove_duplicates(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


llist = LinkedList()
llist.append(1)
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(3)
llist.append(3)
llist.append(4)

print("Original List:")
llist.print_list()

llist.remove_duplicates()

print("List after removing duplicates:")
llist.print_list()
