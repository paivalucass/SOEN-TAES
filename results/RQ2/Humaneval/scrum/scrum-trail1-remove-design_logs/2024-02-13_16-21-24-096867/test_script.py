def match_parens(lst):
    stack = []
    for s in lst:
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if not stack or stack.pop() != '(': return 'No'
    return 'Yes'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(['()(', ')']), 'Yes')
        self.assertEqual(function_under_test([')', ')']), 'No')

if __name__ == '__main__':
    unittest.main()