def first_repeated_char(str1):
    if not str1:
        return "Input string is empty"

    char_freq = {}
    for char in str1:
        if char in char_freq:
            return char
        else:
            char_freq[char] = 1

    return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_repeated_char('abcabc'), 'a')

if __name__ == '__main__':
    unittest.main()