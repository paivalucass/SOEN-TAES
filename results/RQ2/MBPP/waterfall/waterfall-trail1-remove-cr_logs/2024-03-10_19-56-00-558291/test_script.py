def sum_range_list(list1, m, n):
    total_sum = sum(list1[m:n+1])
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10), 29)

if __name__ == '__main__':
    unittest.main()