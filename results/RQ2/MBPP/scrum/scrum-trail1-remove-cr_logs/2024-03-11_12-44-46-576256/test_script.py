def sum(a, b):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    def common_divisors(x, y):
        g = gcd(x, y)
        result = 0
        for i in range(1, g+1):
            if x % i == 0 and y % i == 0:
                result += i
        return result
    
    return common_divisors(a, b)
import unittest

class Test(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(10, 15), 6)

if __name__ == '__main__':
    unittest.main()