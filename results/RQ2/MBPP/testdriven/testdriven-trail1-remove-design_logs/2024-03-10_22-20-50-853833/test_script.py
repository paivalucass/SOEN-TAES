def count_occurrences_of_std(input_string):
    return input_string.count('std')
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_occurance('letstdlenstdporstd'), 3)

if __name__ == '__main__':
    unittest.main()