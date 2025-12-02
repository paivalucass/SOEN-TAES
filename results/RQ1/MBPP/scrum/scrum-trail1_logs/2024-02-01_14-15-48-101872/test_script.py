def max_difference(test_list):
    if len(test_list) < 2:
        return 0
    max_diff = float('-inf')
    min_val = test_list[0][0]
    for pair in test_list:
        min_val = min(min_val, pair[0])
        max_diff = max(max_diff, pair[1] - min_val)
    return max_diff

assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 6
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]), 7)

if __name__ == '__main__':
    unittest.main()