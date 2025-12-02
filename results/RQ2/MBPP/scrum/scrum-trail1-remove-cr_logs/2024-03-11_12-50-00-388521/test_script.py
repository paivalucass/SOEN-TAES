def sum_range_list(list1, m, n):
    total_sum = 0
    try:
        for num in list1[m:n+1]:
            total_sum += num
        return total_sum
    except:
        return "Invalid input range"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10), 29)

if __name__ == '__main__':
    unittest.main()