from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    stack = []
    result = []
    depth = 0
    for c in paren_string:
        if c == '(': 
            stack.append(c)
            depth = max(depth, len(stack))
        elif c == ')': 
            stack.pop()
        if c == ' ': 
            result.append(depth)
            depth = 0
    result.append(depth)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

if __name__ == '__main__':
    unittest.main()