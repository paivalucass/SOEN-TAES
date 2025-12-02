def match_parens(lst):
    stack = []
    concatenated_string = ''.join(lst)
    
    for char in concatenated_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return 'No'
            else:
                stack.pop()
        else:
            return 'Invalid input'
    
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