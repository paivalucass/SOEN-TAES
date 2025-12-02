def max_difference(test_list):
    if len(test_list) < 2:
        return 0
    sorted_list = sorted(test_list, key=lambda x: abs(x[0] - x[1]))
    diff_list = [abs(pair[0] - pair[1]) for pair in sorted_list]
    return max(diff_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]), 7)

if __name__ == '__main__':
    unittest.main()