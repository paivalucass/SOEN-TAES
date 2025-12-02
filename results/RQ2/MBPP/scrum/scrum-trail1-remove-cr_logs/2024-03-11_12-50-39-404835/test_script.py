def count_occurrence(s):
    return s.count('std')
import unittest

class Test(unittest.TestCase):
    def test_count_occurance(self):
        self.assertEqual(count_occurance("letstdlenstdporstd"), 3)

if __name__ == '__main__':
    unittest.main()