def count_char_position(str1):
    if not str1:
        return 0
    
    count = 0
    for i in range(len(str1)):
        char = str1[i].lower()
        if char.isalpha() and ord(char) - ord('a') == i:
            count += 1
    
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_char_position('xbcefg'), 2)

if __name__ == '__main__':
    unittest.main()