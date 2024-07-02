from stack import Stack


# 1. Reverse String
def reverse_string(string):
    if string is None:
        raise AttributeError("Invalid Argument")
    stack = Stack()
    reversed = []
    for char in string:
        stack.push(char)
    for i in range(stack.length):
        reversed.append(stack.pop())
    return "".join(reversed)


# Testing
string = "Hello, World!"
print(reverse_string(string))


# 2. Balnced Expression
def is_balanced(string):
    if string is None:
        raise AttributeError("Invalid Argument")
    BRACES = "{}[]()<>"
    PAIRS = {"{": "}", "[": "]", "(": ")", "<": ">"}
    stack = Stack()
    for char in string:
        if char in BRACES:
            if char in PAIRS:
                stack.push(PAIRS[char])
            elif stack.is_empty():
                return False
            elif stack.pop() != char:
                return False
    if stack.is_empty():
        return True
    return False


# Testing
string = "{({melvin})}"
print(is_balanced(string))
