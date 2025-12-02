def count_char_position(input_string: str) -> int:
    matching_count = 0
    for index, char in enumerate(input_string):
        lowercase_char = char.lower()
        if ord(lowercase_char) - ord('a') == index:
            matching_count += 1
    return matching_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_char_position('xbcefg'), 2)

if __name__ == '__main__':
    unittest.main()