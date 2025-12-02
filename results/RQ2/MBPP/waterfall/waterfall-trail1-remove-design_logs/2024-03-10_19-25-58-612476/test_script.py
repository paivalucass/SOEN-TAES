def check_expression(exp):
    stack = []
    opening = "({["
    closing = ")}]"
    pairs = {")": "(", "}": "{", "]": "["}
    
    for char in exp:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            if stack[-1] == pairs[char]:
                stack.pop()
            else:
                return False
    
    return not stack
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_expression('{()}[{}]'), True)

if __name__ == '__main__':
    unittest.main()