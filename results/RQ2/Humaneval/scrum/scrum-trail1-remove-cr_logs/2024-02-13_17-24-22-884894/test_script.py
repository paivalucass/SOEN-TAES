from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def insert(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True

def all_prefixes(string: str) -> List[str]:
    root = TrieNode()
    result = []
    prefix = ""
    for char in string:
        prefix += char
        insert(root, prefix)
    
    def find_prefixes(node, prefix):
        if node.is_end_of_word:
            result.append(prefix)
        for char, child_node in node.children.items():
            find_prefixes(child_node, prefix + char)

    find_prefixes(root, "")
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

if __name__ == '__main__':
    unittest.main()