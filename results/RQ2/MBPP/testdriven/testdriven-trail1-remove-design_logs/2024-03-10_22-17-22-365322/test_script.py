def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum+1):
        if all(int(digit) != 0 and num % int(digit) == 0 for digit in str(num)):
            result.append(num)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(divisible_by_digits(1, 22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])

if __name__ == '__main__':
    unittest.main()