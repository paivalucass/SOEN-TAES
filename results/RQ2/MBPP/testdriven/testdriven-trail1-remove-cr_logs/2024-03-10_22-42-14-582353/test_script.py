def cal_sum(n):
    perrin = [3, 0, 2]
    for i in range(3, n+1):
        perrin.append(perrin[i-2] + perrin[i-3])
    return perrin[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cal_sum(9), 49)

if __name__ == '__main__':
    unittest.main()