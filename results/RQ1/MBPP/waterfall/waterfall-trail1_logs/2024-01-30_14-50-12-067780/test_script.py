def cumulative_sum(test_list):
    total_sum = sum(chain.from_iterable(test_list))
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]), 30)

if __name__ == '__main__':
    unittest.main()