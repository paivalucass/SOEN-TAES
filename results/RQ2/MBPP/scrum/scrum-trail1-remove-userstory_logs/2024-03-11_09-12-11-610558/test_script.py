def cal_sum(n):
    perrin = [3, 0, 2]
    if n <= 3:
        return sum(perrin[:n])
    else:
        for i in range(3, n):
            perrin.append(perrin[-2] + perrin[-3])
        return sum(perrin)
import unittest

class Test(unittest.TestCase):
    def test_cal_sum(self):
        self.assertEqual(cal_sum(9), 49)

if __name__ == '__main__':
    unittest.main()