def max_sum_list(lists):
    max_sum = float('-inf')
    max_list = []
    for l in lists:
        if sum(l) > max_sum:
            max_sum = sum(l)
            max_list = l
    return max_list
import unittest

class Test(unittest.TestCase):
    def test_max_sum_list(self):
        self.assertEqual(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]), [10, 11, 12])

if __name__ == '__main__':
    unittest.main()