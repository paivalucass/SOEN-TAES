def cal_sum(n): 
    perrin_numbers = [3, 0, 2]
    if n == 1:
        return perrin_numbers[0]
    elif n == 2:
        return perrin_numbers[1]
    elif n == 3:
        return perrin_numbers[2]
    else:
        for i in range(3, n):
            next_num = perrin_numbers[-3] + perrin_numbers[-2]
            perrin_numbers.append(next_num)
        return sum(perrin_numbers)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cal_sum(9), 49)

if __name__ == '__main__':
    unittest.main()