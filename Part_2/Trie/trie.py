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

        def get_children(self):
            return self.children.values()

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
                self.length += 1
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

    def remove(self, word):
        word = word.lower()
        node = self.root
        for char in word:
            if not node.has_child(char):
                print("Word not in the list")
                return
            node = node.get_child(char)
        node.is_end_of_word = False


trie = Trie()
words = [
    "boy",
    "book",
    "border",
    "cat",
    "dog",
    "doctor",
    "fine",
    "fines",
    "finest",
    "figure",
    "pick",
    "pickle",
    "picture",
]
for word in words:
    trie.insert(word)
trie.remove("fine")
print(trie.find("fine"))
