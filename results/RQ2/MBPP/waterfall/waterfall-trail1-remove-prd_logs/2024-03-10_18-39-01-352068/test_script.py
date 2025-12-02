def cal_sum(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input parameter 'n' must be a positive integer")

    if n == 1:
        return 3
    elif n == 2:
        return 0
    elif n == 3:
        return 2

    p1, p2, p3 = 3, 0, 2
    total_sum = p1 + p2 + p3
    for i in range(4, n + 1):
        p_current = p1 + p2 + p3
        total_sum += p_current
        p1, p2, p3 = p2, p3, p_current

    return total_sum
import unittest

class Test(unittest.TestCase):
    def test_cal_sum(self):
        self.assertEqual(cal_sum(9), 49)

if __name__ == '__main__':
    unittest.main()