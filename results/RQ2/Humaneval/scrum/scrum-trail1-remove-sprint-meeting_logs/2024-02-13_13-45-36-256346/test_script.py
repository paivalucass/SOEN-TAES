from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

def insert(root, key):
    node = root
    for level in range(len(key)):
        index = ord(key[level]) - ord('a')
        if not node.children[index]:
            node.children[index] = TrieNode()
        node = node.children[index]
    node.is_end_of_word = True

def search(root, key):
    node = root
    for level in range(len(key)):
        index = ord(key[level]) - ord('a')
        if not node.children[index]:
            return []
        node = node.children[index]
    return find_prefix_words(node, key)

def find_prefix_words(node, prefix):
    words = []
    if node.is_end_of_word:
        words.append(prefix)
    for i in range(26):
        if node.children[i]:
            char = chr(i + ord('a'))
            words.extend(find_prefix_words(node.children[i], prefix + char))
    return words

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    root = TrieNode()
    for s in strings:
        insert(root, s)
    return search(root, prefix)
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])
        
    def test2(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

if __name__ == '__main__':
    unittest.main()