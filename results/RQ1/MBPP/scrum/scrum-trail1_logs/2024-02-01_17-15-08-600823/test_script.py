def count_char_position(str1):
    count = 0
    for i in range(len(str1)):
        if str1[i].isalpha() and (str1[i].lower() == chr(ord('a') + i) or str1[i].upper() == chr(ord('A') + i)):
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_char_position('xbcefg'), 2)

if __name__ == '__main__':
    unittest.main()