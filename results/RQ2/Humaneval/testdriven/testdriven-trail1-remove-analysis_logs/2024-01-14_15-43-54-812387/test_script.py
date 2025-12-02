from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    for group in paren_string.split():
        stack = []
        max_nesting = 0
        nesting = 0
        for char in group:
            if char == '(':
                stack.append(char)
                nesting += 1
                max_nesting = max(max_nesting, nesting)
            elif char == ')':
                if not stack:
                    return "Invalid input"
                stack.pop()
                nesting -= 1
        if stack:
            return "Unmatched parentheses"
        result.append(max_nesting)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

if __name__ == '__main__':
    unittest.main()