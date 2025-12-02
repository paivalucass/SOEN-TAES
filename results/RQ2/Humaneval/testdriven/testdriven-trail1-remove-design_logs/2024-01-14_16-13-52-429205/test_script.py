from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depths = []
    paren_count = 0
    for char in paren_string:
        if char == '(':n
            paren_count += 1
            depths.append(paren_count)
        elif char == ')':
            paren_count -= 1
            depths.append(paren_count)
        else:
            raise ValueError("Input string contains characters other than '(' and ')'")
    return [x // 2 for x in depths if x % 2 == 0]

import unittest
from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

if __name__ == '__main__':
    unittest.main()