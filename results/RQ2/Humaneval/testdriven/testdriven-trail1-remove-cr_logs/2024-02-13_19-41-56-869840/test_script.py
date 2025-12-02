from typing import List

def all_prefixes(string: str) -> List[str]:
    if not string:
        return []

    prefixes = [string[:i+1] for i in range(len(string))]
    return prefixes

# Test cases
print(all_prefixes('abc'))
print(all_prefixes('a@b#c'))
print(all_prefixes('123'))
print(all_prefixes('abcdefghijklmnopqrstuvwxyz'))
print(all_prefixes('a'))
print(all_prefixes('123$'))
import unittest
from typing import List

class Test(unittest.TestCase):
    def test_all_prefixes(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

if __name__ == '__main__':
    unittest.main()