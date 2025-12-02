def first_repeated_char(str1):
    seen = set()
    for char in str1:
        if char in seen:
            return char
        seen.add(char)
    return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_repeated_char('abcabc'), 'a')

if __name__ == '__main__':
    unittest.main()