class StringUtils:

    # 1. Find the number of vowels in a string. Vowels in English are A, E, O, U and I.
    def count_vowel(self, string):
        VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        count = 0
        if string is None:
            return count
        for letter in string:
            if letter in VOWELS:
                count += 1
        return count

    # 2. Reverse a string.
    def reverse_string(self, string):
        if string is None:
            return ""
        return string[::-1]

    # 3. Reverse the order of words in a sentence.
    def reverse_words(self, string):
        if string is None:
            return ""
        words = string.split(" ")
        reversed_words = words[::-1]
        return " ".join(reversed_words)

    # 4. Check if a string is a rotation of another string.
    def is_rotation(self, string_1, string_2):
        if len(string_1) != len(string_2) or string_1 is None or string_2 is None:
            return False
        if string_2 in (string_1 + string_1):
            return True
        return False

    # 5. Remove duplicate characters in a string.
    def remove_duplicates(self, string):
        if string is None:
            return ""
        seen = set()
        result = []
        for char in string:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return "".join(result)

    # 6. Find the most repeated character in a string.
    def most_repeated_character(self, string):
        if string is None or len(string) == 0:
            raise AttributeError
        char_map = {}
        for char in string:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1
        most_repeated_char = ""
        max_count = 0
        for char, count in char_map.items():
            if count > max_count:
                max_count = count
                most_repeated_char = char
        return most_repeated_char

    # 7. Capitalize the first letter of each word in a sentence. Also, remove any extra spaces between words.
    def capitalize(self, string):
        if string is None:
            raise AttributeError("'NoneType' object has no attribute 'capitalize'")
        words = string.split()
        print(words)
        capitalized_words = [word.capitalize() for word in words]
        return " ".join(capitalized_words)

    # 8. Detect if two strings are anagram of each other. A string is an anagram of another string if it has the exact same characters in any order.
    def is_anagram(self, string_1, string_2):
        if string_1 is None or string_2 is None or len(string_1) != len(string_2):
            return False
        sorted_string_1 = sorted(string_1.upper())
        sorted_string_2 = sorted(string_2.upper())
        return sorted_string_1 == sorted_string_2

    def is_palindrome(self, string):
        if string is None or string == "":
            return False
        string = string.lower()
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def replace_with_nth(self, string):
        result = []
        for char in string:
            if char.isalpha():
                if char.isupper():
                    result.append()
        

string_utils = StringUtils()
string = "Vaada mwone, chettai           paalum          vellam medich                 tharaam."
# print(string_utils.count_vowel(string))
# print(string_utils.reverse_string(string))
# print(string_utils.reverse_words(string))
# string_1 = "      qwertyt"
# string_2 = "      qwertyt"
# print(string_utils.is_rotation_simple(string_1, string_2))
# print(string_utils.remove_duplicates(string))
# print(string_utils.most_repeated_character(string))
# print(string_utils.capitalize(string))
# print(string_utils.is_anagram(string_1, string_2))
string = "a"
print(string_utils.is_palindrome(string))
