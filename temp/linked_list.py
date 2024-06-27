# Linked List

# preppend()
# append()
# remove_first()
# remove_last()
# contains()
# index_of()
# size()
# to_array()
# remove()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        head = self.head
        new_node = Node(data)
        if head is not None:
            new_node.next = head
        else:
            self.tail = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.tail is not None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.prepend(data)

    def remove_first(self):
        head = self.head
        if head is not None:
            self.head = head.next
        else:
            raise Exception("Linked list is empty")

    def remove_last(self):
        second_last_node = self.head
        if second_last_node is not None:
            while second_last_node.next.next is not None:
                second_last_node = second_last_node.next
            second_last_node.next = None
            self.tail = second_last_node
        else:
            raise Exception("Linked list is empty")

    def size(self):
        current_node = self.head
        size = 0
        while current_node is not None:
            size += 1
            current_node = current_node.next
        return size

    def contains(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.data == value:
                return True
            current_node = current_node.next
        return False

    def index_of(self, value):
        current_node = self.head
        index = -1
        if current_node is not None:
            index += 1
            while current_node is not None:
                if current_node.data == value:
                    return index
                current_node = current_node.next
                index += 1
        return -1

    def to_array(self):
        array = []
        current_node = self.head
        while current_node is not None:
            array.append(current_node.data)
            current_node = current_node.next
        return array

    def set_tail(self):
        current_node = self.head
        if current_node is not None:
            while current_node is not None:
                if current_node.next == None:
                    self.tail = current_node
                current_node = current_node.next
        else:
            self.tail = None

    def remove(self, value):
        current_node = self.head
        if current_node is not None:
            while current_node.next is not None:
                if current_node.next.data == value:
                    current_node.next = current_node.next.next
                    if current_node.next == None:
                        self.tail = current_node
                    break
                current_node = current_node.next
            else:
                print("Item not found")
        else:
            raise Exception("Linked list is empty")

    def print_list(self):
        current_node = self.head
        print("[", end="")
        while current_node is not None:
            if current_node.next is not None:
                print(current_node.data, end=" -> ")
            else:
                print(f"{current_node.data}", end="")
            current_node = current_node.next
        print("]")

    def get_kth_from_end(self, k):
        if k <= 0:
            raise Exception("Value of k is invalid")
        k -= 1
        right_node = self.head
        left_node = None
        if right_node is not None:
            count = 0
            while right_node is not None:
                if count == k:
                    left_node = self.head
                if count > k:
                    left_node = left_node.next
                count += 1
                right_node = right_node.next
            print(count)
            if count <= k:
                raise Exception("Not enough elements")
            else:
                return left_node.data
        else:
            raise Exception("Linked list is empty")

    def insert_after(self, value, key):
        new_node = Node(value)
        current_node = self.head
        if current_node is not None:
            while current_node is not None:
                if current_node.data == key:
                    new_node.next = current_node.next
                    current_node.next = new_node
                    if new_node.next == None:
                        self.tail = new_node
                    break
                current_node = current_node.next
            else:
                raise Exception("key not found")
        else:
            raise Exception("Linked list is empty")

    def insert_before(self, value, key):
        new_node = Node(value)
        current_node = self.head
        previous_node = None
        if current_node.data == key:
            new_node.next = current_node
            self.head = new_node
            return
        if current_node is not None:
            while current_node is not None:
                if current_node.data == key:
                    previous_node.next = new_node
                    new_node.next = current_node
                    break
                previous_node = current_node
                current_node = current_node.next
            else:
                raise Exception("key not found")
        else:
            raise Exception("Linked list is empty")

    def reverse(self):
        current_node = self.head
        previous_node = None
        if current_node is not None:
            self.tail = current_node
            while current_node is not None:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
            self.head = previous_node

    def print_reverse(self):
        new_ll = LinkedList()
        new_ll.head = self.head
        new_ll.reverse()
        new_ll.print_list()
        del new_ll

    def remove_duplicates(self):
        current_node = self.head
        previous_node = self.head
        if current_node is not None:
            while current_node is not None:
                if current_node == self.head:
                    current_node = current_node.next
                    continue
                if current_node.data == previous_node.data:
                    self.remove(current_node.data)
                previous_node = current_node
                current_node = current_node.next


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(30)
linked_list.append(40)
linked_list.append(40)
linked_list.append(50)
linked_list.append(60)
linked_list.append(70)
linked_list.append(70)
linked_list.print_list()
linked_list.remove_duplicates()
linked_list.print_list()
