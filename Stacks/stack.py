# Building Stack from scratch
class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, item):
        self.stack.append(item)
        self.length += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        deleted_item = self.stack.pop()
        self.length -= 1
        return deleted_item

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.stack[-1]

    def print_stack(self):
        print(self.stack)


# stack = Stack()
# print(stack.is_empty())
# stack.print_stack()
# stack.push(10)
# print(stack.is_empty())
# stack.push(20)
# stack.push(30)
# stack.print_stack()
# print(stack.pop())
# print(stack.pop())
# stack.push(40)
# stack.push(50)
# stack.print_stack()
# print(stack.peek())
