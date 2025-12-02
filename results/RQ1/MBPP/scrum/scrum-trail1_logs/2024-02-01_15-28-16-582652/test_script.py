def first_non_repeating_character(str1):
    char_frequency = {}
    for char in str1:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    for char in str1:
        if char_frequency[char] == 1:
            return char
    return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_non_repeating_character('abcabc'), None)

if __name__ == '__main__':
    unittest.main()