def fix_spaces(text):
    result = ''
    consecutive_spaces = 0
    for char in text:
        if char == ' ':
            consecutive_spaces += 1
            if consecutive_spaces > 2:
                result = result[:-1] + '-'
            else:
                result += '_'
        else:
            consecutive_spaces = 0
            result += char
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(fix_spaces("Example"), "Example")
        self.assertEqual(fix_spaces("Example 1"), "Example_1")
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")

if __name__ == '__main__':
    unittest.main()