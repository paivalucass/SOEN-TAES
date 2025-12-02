def cal_sum(n):
    perrin_numbers = [3, 0, 2]
    for i in range(3, n):
        perrin_numbers.append(perrin_numbers[i-3] + perrin_numbers[i-2])
    sum_perrin = sum(perrin_numbers[:n])
    return sum_perrin
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cal_sum(9), 49)

if __name__ == '__main__':
    unittest.main()