def match_parens(lst):
    stack = []
    for string in lst:
        for char in string:
            if char == '(':
                stack.append(char)
            else:
                if not stack:
                    return 'No'
                stack.pop()
    if not stack:
        return 'Yes'
    else:
        return 'No'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(match_parens(['()(', ')']), 'Yes')
        self.assertEqual(match_parens([')', ')']), 'No')

if __name__ == '__main__':
    unittest.main()