def match_parens(lst):
    stack = []
    for s in lst:
        for char in s:
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
        self.assertEqual(function_under_test(['()(', ')']), 'Yes')
        self.assertEqual(function_under_test([')', ')']), 'No')

if __name__ == '__main__':
    unittest.main()