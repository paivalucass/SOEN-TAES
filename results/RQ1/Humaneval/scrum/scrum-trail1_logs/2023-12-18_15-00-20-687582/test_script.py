from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._get_all_words_from_node(node, prefix)

    def _get_all_words_from_node(self, node, prefix):
        result = []
        if node.is_end_of_word:
            result.append(prefix)
        for char in node.children:
            result += self._get_all_words_from_node(node.children[char], prefix + char)
        return result

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    trie = Trie()
    for word in strings:
        trie.insert(word)
    return trie.search_prefix(prefix)
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_with_prefix_a(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

if __name__ == '__main__':
    unittest.main()