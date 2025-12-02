def max_difference(test_list):
    if not isinstance(test_list, list) or not all(isinstance(item, tuple) for item in test_list):
        raise ValueError("Input must be a list of tuples")

    max_diff = 0
    for tup in test_list:
        if len(tup) != 2:
            raise ValueError("Each tuple must contain exactly 2 elements")
        diff = abs(tup[0] - tup[1])
        if diff > max_diff:
            max_diff = diff

    return max_diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]), 7)

if __name__ == '__main__':
    unittest.main()