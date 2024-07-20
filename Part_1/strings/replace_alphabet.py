def replace_alphabet(string, n):
    result = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in string:
        if char.isalpha():
            is_upper = char.isupper()
            char_lower = char.lower()
            index = (alphabet.index(char_lower) + n) % 26
            new_char = alphabet[index]
            result.append(new_char.upper() if is_upper else new_char)
        else:
            result.append(char)
    return "".join(result)


input_string = "Hello, World!"
n = 3
print("Original string:", input_string)
print(f"After replacing each alphabet with {n}-th position alphabet:")
print(replace_alphabet(input_string, n))
