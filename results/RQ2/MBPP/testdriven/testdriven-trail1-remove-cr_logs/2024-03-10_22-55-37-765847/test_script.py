def count_char_position(str1):
    count = 0
    if str1 is not None and str1 != '':
        str1 = str1.lower()
        for i in range(len(str1)):
            if str1[i].isalpha() and ord(str1[i]) - ord('a') == i:
                count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_char_position('xbcefg'), 2)

if __name__ == '__main__':
    unittest.main()