def check_expression(exp):
    stack = []
    mapping = {"(": ")", "{": "}", "[": "]"}
    for char in exp:
        if char in mapping:
            stack.append(char)
        else:
            if not stack or mapping[stack.pop()] != char:
                return False
    return not stack
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_expression("{()}[{}]"), True)

if __name__ == '__main__':
    unittest.main()