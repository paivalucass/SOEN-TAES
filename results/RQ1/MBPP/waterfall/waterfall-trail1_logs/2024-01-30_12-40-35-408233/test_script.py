def count_char_position(input_string: str) -> int:
    if not input_string:
        return 0

    count = 0
    input_string = input_string.lower()
    for index in range(len(input_string)):
        if input_string[index].isalpha() and ord(input_string[index]) - ord('a') == index:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_char_position('xbcefg'), 2)

if __name__ == '__main__':
    unittest.main()