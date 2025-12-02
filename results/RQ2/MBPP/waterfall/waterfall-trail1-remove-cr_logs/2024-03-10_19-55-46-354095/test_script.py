def count_char_position(str1):
    if not isinstance(str1, str):
        raise ValueError("Input is not a valid string")

    count = 0
    for char in str1:
        if char.isalpha():
            char_value = ord(char.lower()) - 96
            if char_value == (str1.index(char.lower()) + 1):
                count += 1

    return count
import unittest

class Test(unittest.TestCase):
    def test_count_char_position(self):
        self.assertEqual(count_char_position('xbcefg'), 2)

if __name__ == '__main__':
    unittest.main()