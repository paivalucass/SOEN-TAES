from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    count = 0
    max_count = 0
    for char in paren_string:
        if char == '(': 
            count += 1
            max_count = max(max_count, count)
        elif char == ')':
            count -= 1
        elif char == ' ': 
            result.append(max_count)
            max_count = 0
    result.append(max_count)
    return result
import unittest
from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

if __name__ == '__main__':
    unittest.main()