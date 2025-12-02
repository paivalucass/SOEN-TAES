from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    stack = []
    max_depth = 0
    for char in paren_string:
        if char == '(':
            stack.append(char)
            max_depth = max(max_depth, len(stack))
        elif char == ')':
            stack.pop()
        elif char == ' ':
            depths.append(max_depth)
            max_depth = 0
    depths.append(max_depth)
    return depths
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

if __name__ == '__main__':
    unittest.main()