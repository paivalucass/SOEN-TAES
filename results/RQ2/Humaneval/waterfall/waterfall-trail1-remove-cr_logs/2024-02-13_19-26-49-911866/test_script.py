from typing import List

def match_parens(lst: List[str]) -> str:
    if len(lst) != 2 or not all(isinstance(s, str) for s in lst):
        return 'Invalid input'

    combined_string = lst[0] + lst[1]

    stack = []
    for char in combined_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return 'No'
            stack.pop()

    return 'Yes' if not stack else 'No'
import unittest

class Test(unittest.TestCase):
    def test_match_parens(self):
        self.assertEqual(match_parens(['()(', ')']), 'Yes')
        self.assertEqual(match_parens([')', ')']), 'No')

if __name__ == '__main__':
    unittest.main()