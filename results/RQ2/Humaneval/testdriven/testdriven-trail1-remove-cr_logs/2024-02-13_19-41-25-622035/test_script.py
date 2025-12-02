from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    depth = 0
    for char in paren_string:
        if char == '(': 
            depth += 1
        elif char == ')':
            depth -= 1
        depths.append(depth)
    return depths
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

if __name__ == '__main__':
    unittest.main()