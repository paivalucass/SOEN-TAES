def cummulative_sum(test_list):
    return sum([sum(tup) for tup in test_list])
import unittest

class Test(unittest.TestCase):
    def test_cummulative_sum(self):
        self.assertEqual(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]), 30)

if __name__ == '__main__':
    unittest.main()