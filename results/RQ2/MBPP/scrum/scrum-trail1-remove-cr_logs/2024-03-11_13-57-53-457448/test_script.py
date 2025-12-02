def divisible_by_digits(startnum, endnum):
    def is_divisible_by_digits(num):
        for digit in str(num):
            if int(digit) == 0 or num % int(digit) != 0:
                return False
        return True
    
    result = []
    for i in range(startnum, endnum+1):
        if is_divisible_by_digits(i):
            result.append(i)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(divisible_by_digits(1, 22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])

if __name__ == '__main__':
    unittest.main()