from typing import List

def all_prefixes(string: str) -> List[str]:
    if not isinstance(string, str):
        raise TypeError("Input must be a string")

    if not string:
        return []

    prefixes = [string[:i+1] for i in range(len(string))]
    return prefixes
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

if __name__ == '__main__':
    unittest.main()