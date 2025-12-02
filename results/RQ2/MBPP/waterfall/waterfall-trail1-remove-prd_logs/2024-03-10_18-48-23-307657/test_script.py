def check_expression(exp):
    stack = []
    mappings = {"(": ")", "{": "}", "[": "]"}
    
    for char in exp:
        if char in mappings:
            stack.append(char)
        elif char in mappings.values():
            if not stack:
                return False
            if mappings[stack.pop()] != char:
                return False
    
    return not stack
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_expression('{()}[{}]'), True)

if __name__ == '__main__':
    unittest.main()