def first_non_repeating_character(str1):
    from collections import Counter
    char_count = Counter(str1)
    for char in str1:
        if char_count[char] == 1:
            return char
    return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_non_repeating_character('abcabc'), None)

if __name__ == '__main__':
    unittest.main()