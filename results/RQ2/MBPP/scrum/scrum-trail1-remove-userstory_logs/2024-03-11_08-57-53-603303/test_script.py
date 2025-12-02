def count_char_position(str1):
    count = 0
    str1 = str1.lower()
    for i in range(len(str1)):
        if ord(str1[i]) - 96 == i + 1:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_char_position('xbcefg'), 2)

if __name__ == '__main__':
    unittest.main()