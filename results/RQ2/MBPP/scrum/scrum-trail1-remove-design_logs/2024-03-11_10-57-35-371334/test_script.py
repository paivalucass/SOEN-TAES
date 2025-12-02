def first_repeated_char(str1):
    char_count = {}
    for char in str1:
        if char in char_count:
            return char
        char_count[char] = 1
    return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_repeated_char('abcabc'), 'a')

if __name__ == '__main__':
    unittest.main()