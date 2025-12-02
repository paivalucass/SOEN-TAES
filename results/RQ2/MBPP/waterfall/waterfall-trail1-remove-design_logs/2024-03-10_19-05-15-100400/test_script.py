def get_Char(input_string):
    total_ascii_sum = 0
    for char in input_string:
        total_ascii_sum += ord(char)
    return chr(((total_ascii_sum - len(input_string)*97) % 26) + 97)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Char('abc'), 'f')

if __name__ == '__main__':
    unittest.main()