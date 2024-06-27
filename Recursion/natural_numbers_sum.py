def sum_of_natural_numbers(n):

    if n == 0:
        return 0

    return n + sum_of_natural_numbers(n - 1)


n = 5
print(f"Sum of first {n} natural numbers:", sum_of_natural_numbers(n))
