from typing import List

def all_prefixes(string: str) -> List[str]:
    return [string[:i+1] for i in range(len(string))] if string else []

# Test with different input strings to ensure correctness
print(all_prefixes('abc')) # Output: ['a', 'ab', 'abc']
print(all_prefixes('')) # Output: []
print(all_prefixes('d')) # Output: ['d']
print(all_prefixes('test')) # Output: ['t', 'te', 'tes', 'test']
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

if __name__ == '__main__':
    unittest.main()