def match_parens(lst):
    open_parens = lst[0]
    close_parens = lst[1]
    stack = []
    
    for char in open_parens:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                return 'No'
            stack.pop()
    
    for char in close_parens:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                return 'No'
            stack.pop()
    
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(match_parens(['()(', ')']), 'Yes')

if __name__ == '__main__':
    unittest.main()