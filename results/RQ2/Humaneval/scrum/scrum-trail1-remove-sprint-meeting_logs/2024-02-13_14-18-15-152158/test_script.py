def match_parens(lst):
    if not lst or len(lst) != 2:
        return 'No'

    if not all(char in '()' for string in lst for char in string):
        return 'No'

    stack = []
    for string in lst:
        for char in string:
            if char == '(':
                stack.append(char)
            else:
                if not stack:
                    return 'No'
                stack.pop()
    
    if stack:
        return 'No'
    else:
        return 'Yes'
import unittest

class Test(unittest.TestCase):
    def test_match_parens(self):
        self.assertEqual(match_parens(['()(', ')']), 'Yes')
        self.assertEqual(match_parens([')', ')']), 'No')

if __name__ == '__main__':
    unittest.main()