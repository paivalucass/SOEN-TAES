def cal_sum(n):
    perrin_numbers = [3, 0, 2]
    if n <= 2:
        return perrin_numbers[n]
    else:
        return cal_sum(n-2) + cal_sum(n-3) + cal_sum(n-4)
import unittest

class Test(unittest.TestCase):
    def test_cal_sum(self):
        self.assertEqual(cal_sum(9), 49)

if __name__ == '__main__':
    unittest.main()