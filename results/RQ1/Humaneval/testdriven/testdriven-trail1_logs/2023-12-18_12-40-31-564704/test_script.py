def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
    return bool(stack)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_nested('[[]]'))
        self.assertFalse(is_nested('[]]]]]]][[[[[]'))
        self.assertFalse(is_nested('[][]'))
        self.assertFalse(is_nested('[]'))
        self.assertTrue(is_nested('[[][]]'))
        self.assertTrue(is_nested('[[]][['))

if __name__ == '__main__':
    unittest.main()