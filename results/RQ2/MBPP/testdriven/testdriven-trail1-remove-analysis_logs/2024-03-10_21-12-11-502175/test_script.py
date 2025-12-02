def count_char_position(str1):
    count = 0
    for i in range(len(str1)):
        char_lower = str1[i].lower()
        if ord(char_lower) - 96 == i + 1 and char_lower.isalpha():
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_char_position('xbcefg'), 2)

if __name__ == '__main__':
    unittest.main()