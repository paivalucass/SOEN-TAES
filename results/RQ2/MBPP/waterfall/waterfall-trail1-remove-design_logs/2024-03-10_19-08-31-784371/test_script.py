def count_char_position(input_string):
    count = 0
    for i in range(len(input_string)):
        if input_string[i].lower() == chr(ord('a') + i):
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_char_position('xbcefg'), 2)

if __name__ == '__main__':
    unittest.main()