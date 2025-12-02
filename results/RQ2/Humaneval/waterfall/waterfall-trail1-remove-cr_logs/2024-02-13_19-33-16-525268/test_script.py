def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']' and stack:
            stack.pop()
        else:
            return False
    return len(stack) == 0
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