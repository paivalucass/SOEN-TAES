def cal_sum(n):
    if not isinstance(n, int) or n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1:
        return 3
    else:
        a, b, c = 3, 0, 2
        result = 5
        for i in range(3, n+1):
            next_val = a + b
            if next_val < 0:
                return "Overflow error"
            result += next_val
            a, b, c = b, c, next_val
        return result
import unittest

class Test(unittest.TestCase):
    def test_cal_sum(self):
        self.assertEqual(cal_sum(9), 49)

if __name__ == '__main__':
    unittest.main()