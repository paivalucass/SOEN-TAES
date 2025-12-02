def sumofFactors(n):
    if not isinstance(n, int):
        return "Invalid input - non-integer"
    if n < 1:
        return 0
    if n > 10000000000:
        return "Out of range error"
    
    sum = 0
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            sum += i
    return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sumofFactors(18), 26)

if __name__ == '__main__':
    unittest.main()