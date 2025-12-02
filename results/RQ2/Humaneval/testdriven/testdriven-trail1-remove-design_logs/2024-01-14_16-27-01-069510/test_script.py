def is_nested(string):
    count = 0
    for char in string:
        if char == '[':
            count += 1
        elif char == ']' and count > 0:
            count -= 1
        else:
            return False
    return count == 0
import unittest

class Test(unittest.TestCase):
    def test_is_nested(self):
        self.assertEqual(is_nested('[[]]'), True)
        self.assertEqual(is_nested('[]]]]]]][[[[[]'), False)
        self.assertEqual(is_nested('[][]'), False)
        self.assertEqual(is_nested('[]'), False)
        self.assertEqual(is_nested('[[][]]'), True)
        self.assertEqual(is_nested('[[]][['), True)

if __name__ == '__main__':
    unittest.main()