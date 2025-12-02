from typing import List

def all_prefixes(string: str) -> List[str]:
    prefixes = set()
    result = []
    
    if not string:
        return result

    for i in range(len(string)):
        prefix = string[:i+1]
        prefixes.add(prefix)
        result.append(prefix)

    return result
import unittest

from typing import List


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])


if __name__ == '__main__':
    unittest.main()