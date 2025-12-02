def first_repeated_char(input_string):
    char_count = {}
    for char in input_string:
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