def cummulative_sum(test_list):
    try:
        return sum([sum(tup) for tup in test_list])
    except (TypeError, ValueError):
        return "Input list should contain only tuples of integers."

assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]), 30)

if __name__ == '__main__':
    unittest.main()