def check_expression(exp):
    stack = []
    opening_brackets = set(['(', '[', '{'])
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    
    for char in exp:
        if char in opening_brackets:
            stack.append(char)
        else:
            if not stack:
                return False
            if stack[-1] == matching_brackets[char]:
                stack.pop()
            else:
                return False
    
    return len(stack) == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(check_expression("{()}[{}]"))

if __name__ == '__main__':
    unittest.main()