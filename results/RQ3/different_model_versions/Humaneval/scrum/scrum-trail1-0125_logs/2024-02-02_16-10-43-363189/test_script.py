from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def count_nested_parens(group: str) -> int:
        stack = []
        max_depth = 0
        current_depth = 0

        for char in group:
            if char == '(':
                stack.append(char)
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                stack.pop()
                current_depth -= 1

        return max_depth

    groups = paren_string.split()
    deepest_levels = []

    for group in groups:
        deepest_levels.append(count_nested_parens(group))

    return deepest_levels
import unittest

from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

if __name__ == '__main__':
    unittest.main()