# Building Stack from scratch
class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0
        self.minimum = float("inf")

    def is_empty(self):
        return self.length == 0

    def push(self, item):
        self.stack.append(item)
        self.length += 1
        if item < self.minimum:
            self.minimum = item

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
    
    def min(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.minimum



stack = Stack()
print(stack.is_empty())
stack.print_stack()
stack.push(10)
print(stack.is_empty())
stack.push(20)
stack.push(30)
stack.print_stack()
print(stack.pop())
print(stack.pop())
stack.push(40)
stack.push(50)
stack.push(-3)
stack.push(3)
stack.print_stack()
print(stack.peek())
print(stack.min())


class DoubleStack:
    def __init__(self):
        self.stack = []
        self.length_1 = 0
        self.length_2 = 0

    def is_empty_1(self):
        return self.length_1 == 0

    def is_empty_2(self):
        return self.length_2 == 0

    def push_1(self, item):
        self.stack.insert(0, item)
        self.length_1 += 1

    def push_2(self, item):
        self.stack.append(item)
        self.length_2 += 1

    def pop_1(self):
        if self.is_empty_1():
            raise ValueError("Stack is empty")
        pop_item = self.stack.pop(0)
        self.length_1 -= 1
        return pop_item

    def pop_2(self):
        if self.is_empty_2():
            raise ValueError("Stack is empty")
        pop_item = self.stack.pop()
        self.length_2 -= 1
        return pop_item

    def peek_1(self):
        if self.is_empty_1():
            raise ValueError("Stack is empty")
        return self.stack[0]

    def peek_2(self):
        if self.is_empty_1():
            raise ValueError("Stack is empty")
        return self.stack[-1]

    def print_stack_1(self):
        print(self.stack[self.length_1 - 1 :: -1])

    def print_stack_2(self):
        print(self.stack[self.length_1 :])


# Testing
# stack = DoubleStack()
# stack.print_stack_1()
# stack.print_stack_2()
# stack.push_1(10)
# stack.push_2(20)
# stack.push_1(30)
# stack.push_2(40)
# stack.push_1(50)
# stack.push_2(60)
# stack.push_1(70)
# stack.push_1(990)
# stack.push_2(80)
# stack.push_2(90)
# stack.print_stack_1()
# stack.print_stack_2()
# print(stack.peek_1())
# print(stack.peek_2())
