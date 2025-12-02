def cal_sum(n):
    perrin_numbers = [3, 0, 2]
    if not isinstance(n, int) or n <= 0:
        return "Error: Invalid input"
    for _ in range(3, n):
        next_perrin = perrin_numbers[-3] + perrin_numbers[-2]
        perrin_numbers.append(next_perrin)
    return sum(perrin_numbers[:n])
import unittest

class Test(unittest.TestCase):
    def test_cal_sum(self):
        self.assertEqual(cal_sum(9), 49)

if __name__ == '__main__':
    unittest.main()