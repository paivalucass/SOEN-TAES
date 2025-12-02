from typing import List

def all_prefixes(string: str) -> List[str]:
    return [string[:i+1] for i in range(len(string))]
import unittest
from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

if __name__ == '__main__':
    unittest.main()