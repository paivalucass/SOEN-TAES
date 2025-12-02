from typing import List


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def delete(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                return
            node = node.children[char]
        node.is_word = False


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class FilterByPrefix:
    def __init__(self, strings: List[str]):
        self.trie = Trie()
        for string in strings:
            self.trie.insert(string)

    def filter(self, prefix: str) -> List[str]:
        node = self.trie.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._dfs(node, prefix)

    def _dfs(self, node: TrieNode, prefix: str) -> List[str]:
        results = []
        if node.is_word:
            results.append(prefix)
        for char, child_node in node.children.items():
            results.extend(self._dfs(child_node, prefix + char))
        return results


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    filter_instance = FilterByPrefix(strings)
    return filter_instance.filter(prefix)
import unittest

from typing import List

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_filtering(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

if __name__ == '__main__':
    unittest.main()