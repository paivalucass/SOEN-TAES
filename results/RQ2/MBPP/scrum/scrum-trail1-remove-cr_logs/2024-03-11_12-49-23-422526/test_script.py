def count_char_position(str1):
    if not isinstance(str1, str):
        raise TypeError("Input must be a string")
        
    count = 0
    for i in range(len(str1)):
        char = str1[i].lower()
        if ord(char) - ord('a') == i:
            count += 1
            
    return count

assert count_char_position("xbcefg") == 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_char_position('xbcefg'), 2)

if __name__ == '__main__':
    unittest.main()