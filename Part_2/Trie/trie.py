# Trie
# Node
# value: char
# children: Node [26]
# isEndOfWord: boolean
# insert(word: String)
# index = ch - 'a'
# 100 - 97 = 3 (d)


class Trie:
    class TrieNode:
        def __init__(self, char):
            self.value = char
            self.children = {}
            self.is_end_of_word = False

        def has_child(self, char):
            return char in self.children

        def add_child(self, char):
            self.children[char] = Trie.TrieNode(char)

        def get_child(self, char):
            return self.children[char]

        def get_all_children(self):
            return self.children.values()

        def has_any_children(self):
            return not len(self.children) == 0

        def remove_child(self, char):
            del self.children[char]

        def __str__(self):
            return f"value {self.value}"

    def __init__(self):
        self.root = Trie.TrieNode(" ")
        self.length = 0

    def insert(self, word):
        word = word.lower()
        node = self.root
        for char in word:
            if not node.has_child(char):
                node.add_child(char)
            node = node.get_child(char)
        node.is_end_of_word = True

    def find(self, word):
        word = word.lower()
        node = self.root
        for char in word:
            if not node.has_child(char):
                return False
            node = node.get_child(char)
        if not node.is_end_of_word:
            return False
        return True

    # def remove(self, word):
    #     word = word.lower()
    #     node = self.root
    #     for char in word:
    #         if not node.has_child(char):
    #             print("Word not in the list")
    #             return
    #         node = node.get_child(char)
    #     node.is_end_of_word = False

    # def remove(self, word):
    #     word = word.lower()
    #     length = len(word)
    #     first_char_index = word[0]

    #     def post_order(root, char_index):
    #         char = word[char_index]
    #         children = root.get_all_children(root)
    #         if char in children:
    #             post_order(root.get_child(char), char_index + 1)
    #         else:
    #             raise ValueError("Word not found")
    #         if char_index == length - 1:

    def traverse(self):

        def pre_order(root):
            children = root.get_all_children()
            print(root.value)
            for child in children:
                pre_order(child)

        def post_order(root):
            children = root.get_all_children()
            for child in children:
                post_order(child)
            print(root.value)

        pre_order(self.root)

    def remove(self, word):
        def removal(root, index=0):
            if index == length:
                root.is_end_of_word = False
                return
            char = word[index]
            child = root.get_child(char)
            if child is None:
                return
            removal(child, index + 1)
            if not child.has_any_children() and not child.is_end_of_word:
                root.remove_child(char)
                self.length -= 1

        word = word.lower()
        length = len(word)
        removal(self.root)

    def auto_completion(self, prefix):
        def add_word(root , prefix):
            if root.is_end_of_word:
                words.append(prefix)
            children = root.get_all_children()
            for child in children:
                add_word(child, prefix + child.value)

        prefix = prefix.lower()
        words = []
        last_node = self.root
        for char in prefix:
            if last_node.has_child(char):
                last_node = last_node.get_child(char)
        add_word(last_node, prefix)
        return words


trie = Trie()
words = [
    "car",
    "care",
    "careful",
    "cargo",
    "egg",
    # "boy",
    # "book",
    # "border",
    # "cat",
    # "dog",
    # "doctor",
    # "fine",
    # "fines",
    # "finest",
    # "figure",
    # "pick",
    # "pickle",
    # "picture",
]
for word in words:
    trie.insert(word)
# print(trie.find("fine"))
# trie.delete("finest")
# trie.find("finest")
# trie.traverse()
# trie.remove("cargo")
# print(trie.find("cargo"))

# print(trie.find("car"))
print(trie.auto_completion("car"))
