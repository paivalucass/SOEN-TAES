def first_repeated_char(str1):
    char_set = set()
    for char in str1:
        if char in char_set:
            return char
        else:
            char_set.add(char)
    return ""
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_repeated_char('abcabc'), 'a')

if __name__ == '__main__':
    unittest.main()