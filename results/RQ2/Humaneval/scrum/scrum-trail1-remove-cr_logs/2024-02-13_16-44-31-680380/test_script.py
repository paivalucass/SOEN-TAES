from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    max_depth = 0
    stack = []

    for group in paren_string.split():
        group_depth = 0
        for char in group:
            if char == '(':
                stack.append(char)
                group_depth = max(group_depth, len(stack))
            elif char == ')':
                stack.pop()
        depths.append(group_depth)

    return depths
import unittest
from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

if __name__ == '__main__':
    unittest.main()