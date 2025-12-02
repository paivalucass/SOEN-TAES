def cummulative_sum(test_list):
    try:
        total_sum = 0
        for each_tuple in test_list:
            for value in each_tuple:
                total_sum += value
        return total_sum
    except (TypeError, ValueError):
        raise Exception("Invalid input")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]), 30)

if __name__ == '__main__':
    unittest.main()