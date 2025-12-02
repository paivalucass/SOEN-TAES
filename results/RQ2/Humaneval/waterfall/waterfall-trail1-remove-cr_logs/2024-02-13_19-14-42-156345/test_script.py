from typing import List

def all_prefixes(string: str) -> List[str]:
    result = [string[:i] for i in range(1, len(string) + 1)]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

if __name__ == '__main__':
    unittest.main()