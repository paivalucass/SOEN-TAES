from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    levels = []
    for group in paren_string.split():
        stack = []
        max_level = 0
        for p in group:
            if p == '(': 
                stack.append(p)
                max_level = max(max_level, len(stack))
            elif p == ')':
                stack.pop()
        levels.append(max_level)
    return levels
import unittest

from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])
        self.assertEqual(parse_nested_parens('()()()() ()()()() ()()()()'), [1, 1, 1, 1, 1, 1])
        self.assertEqual(parse_nested_parens('((((()))))) ((())) () ((())()())'), [9, 3, 1, 3])

if __name__ == '__main__':
    unittest.main()