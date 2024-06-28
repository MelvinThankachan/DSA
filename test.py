def reverse_string(string, i = 0):
    if i == len(string) - 1:
        return string[i]
    return reverse_string(string, i+1) + string[i]


def remove(value):
    current_node = self.head
    if current_node.data == value:
        current_node.prev = None
        self.head = current_node.next
        return
    while current_node is not None:
        if current_node.data == value:
            previous_node = current_node.prev
            next_node = current_node.next
            previous_node.next = next_node
            next_node.prev = previous_node
        current_node = current_node.next

def remove_duplicates(arr):
    result = []
    element_map = set()
    for element in arr:
        if element not in element_map:
            result.append(element)
            element_map.add(element)
    return result