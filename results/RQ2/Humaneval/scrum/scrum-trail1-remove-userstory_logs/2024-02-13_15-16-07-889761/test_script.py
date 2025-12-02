def sum_of_digits_of_largest_prime(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = 0
    for num in lst:
        if is_prime(num) and num > max_prime:
            max_prime = num
    if max_prime == 0:
        return 0
    else:
        return sum(int(i) for i in str(max_prime))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]), 10)
        self.assertEqual(function_under_test([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]), 25)
        self.assertEqual(function_under_test([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]), 13)
        self.assertEqual(function_under_test([0,724,32,71,99,32,6,0,5,91,83,0,5,6]), 11)
        self.assertEqual(function_under_test([0,81,12,3,1,21]), 3)
        self.assertEqual(function_under_test([0,8,1,2,1,7]), 7)

if __name__ == '__main__':
    unittest.main()