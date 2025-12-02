def match_parens(lst):
    stack = []
    for s in lst:
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return 'No'
    return 'Yes' if not stack else 'No'
import unittest

class Test(unittest.TestCase):
    def test_match_parens(self):
        self.assertEqual(match_parens(['()(', ')']), 'Yes')
        self.assertEqual(match_parens([')', ')']), 'No')

if __name__ == '__main__':
    unittest.main()