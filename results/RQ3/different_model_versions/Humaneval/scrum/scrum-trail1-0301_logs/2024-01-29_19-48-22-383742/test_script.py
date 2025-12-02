from typing import List

def all_prefixes(string: str) -> List[str]:
    prefixes = []
    for i in range(1, len(string)+1):
        prefixes.append(string[:i])
    return prefixes
import unittest

from typing import List

class Test(unittest.TestCase):

    def test_all_prefixes(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])
        self.assertEqual(all_prefixes(''), [])

if __name__ == '__main__':
    unittest.main()