def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']' and stack:
            stack.pop()
        else:
            return False
    return not stack
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_nested('[[]]'), True)
        self.assertEqual(is_nested('[]]]]]]][[[[[]'), False)
        self.assertEqual(is_nested('[][]'), False)
        self.assertEqual(is_nested('[]'), False)
        self.assertEqual(is_nested('[[][]]'), True)
        self.assertEqual(is_nested('[[]][['), True)

if __name__ == '__main__':
    unittest.main()