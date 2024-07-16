def print_reverse(n):
    print(n)
    if n == 1:
        return
    return print_reverse(n - 1)


# print_reverse(10)


# Program to add a item in the bottom of a stack
def push_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
        return
    pop_item = stack.pop()
    push_bottom(stack, item)
    stack.append(pop_item)
    return stack


# stack = [1, 2, 3, 4]
# item = 5
# print(push_bottom(stack, item))
# print(stack)


# Reverse a stack
def reverse_stack(stack, prev=None):
    if len(stack) <= 1:
        return stack
    pop_item = stack.pop()
    reversed_stack = reverse_stack(stack, pop_item)
    reversed_stack.append(prev)
    return reversed_stack


stack = [1, 2, 3, 4]
print(reverse_stack(stack))
