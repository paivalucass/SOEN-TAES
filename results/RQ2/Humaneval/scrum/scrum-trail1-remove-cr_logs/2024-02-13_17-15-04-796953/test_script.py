def is_nested(string):
    count = 0
    for char in string:
        if char == '[':
            count += 1
        elif char == ']':
            count -= 1
        if count < 0:
            return False
    return count == 0
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