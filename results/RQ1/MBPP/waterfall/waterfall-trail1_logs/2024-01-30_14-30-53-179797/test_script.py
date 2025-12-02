def cal_sum(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input value 'n' must be a positive integer")

    perrin_sum = 0
    perrin_numbers = [3, 0, 2]

    for i in range(3, n + 1):
        perrin_sum += perrin_numbers[i % 3]
        perrin_numbers[i % 3] = perrin_numbers[(i - 1) % 3] + perrin_numbers[(i - 2) % 3]

    return perrin_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cal_sum(9), 49)

if __name__ == '__main__':
    unittest.main()