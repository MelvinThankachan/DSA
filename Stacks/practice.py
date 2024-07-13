# Implement a stack using arrays (lists) in Python, and write functions for push, pop, and peek operations.
class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.empty():
            return None
        return self.stack[-1]


# Write a function to check if parentheses in a given string are balanced using a stack.
def is_balanced(s):
    BRACES = "{[(<>)]}"
    PAIRS = {"{": "}", "(": ")", "[": "]", "<": ">"}
    tracking = []
    for char in s:
        if char in BRACES:
            if char in PAIRS:
                tracking.append(PAIRS[char])
            elif not tracking or char != tracking.pop():
                return False
    if tracking:
        return False
    return True


# Implement a stack-based algorithm to convert a given infix expression (containing +, -, *, /, (, and )) to postfix notation.
def postfix(s):
    OPERANDS = "+-*/"
    BRACES = "()"
    postfix_output = ""
    operand_stack = []
    for char in s:
        if char in BRACES:
            continue
        if char in OPERANDS:
            operand_stack.append(char)
        else:
            postfix_output += char
    while operand_stack:
        postfix_output += operand_stack.pop()
    return postfix_output


# Implement a function to reverse a stack without using extra space
def reverse(stack):
    if len(stack) <= 1:
        return stack
    pop_item = stack.pop()
    return [pop_item] + reverse(stack)


# Implement a stack using queues
from collections import deque


class Stack:
    def __init__(self):
        self.queue = deque()
        self.temp_queue = deque()
    
    def is_empty(self):
        return len(self.queue) == 0

    def push(self, item):
        self.queue.append(item)
    
    def pop(self):
        if self.is_empty(): return None
        while len(self.queue) > 1:
            self.temp_queue.append(self.queue.popleft())
        
        last_item = self.queue.popleft()

        while self.temp_queue:
            self.queue.append(self.temp_queue.popleft())

        return last_item
    
    def peek(self):
        if self.is_empty(): return None
        return self.queue[0]