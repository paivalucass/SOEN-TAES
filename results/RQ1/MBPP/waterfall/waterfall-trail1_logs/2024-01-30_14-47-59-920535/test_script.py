def first_repeated_char(str1):
    if not isinstance(str1, str) or len(str1) < 2:
        return None

    chars = set()
    for char in str1:
        if char in chars:
            return char
        else:
            chars.add(char)
    return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_repeated_char('abcabc'), 'a')

if __name__ == '__main__':
    unittest.main()