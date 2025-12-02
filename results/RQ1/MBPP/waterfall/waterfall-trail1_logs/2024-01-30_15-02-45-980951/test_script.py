def divisible_by_digits(startnum, endnum):
    result_list = []
    for num in range(startnum, endnum + 1):
        digits = [int(d) for d in str(num) if int(d) != 0 and num % int(d) == 0]
        if len(digits) == len(str(num)):
            result_list.append(num)
    return result_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(divisible_by_digits(1, 22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])

if __name__ == '__main__':
    unittest.main()