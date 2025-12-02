def sumOfFactors(n):
    evenFactorsSum = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                evenFactorsSum += i
            if (n // i) % 2 == 0 and (n // i) != i:
                evenFactorsSum += n // i
    return evenFactorsSum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sumofFactors(18), 26)

if __name__ == '__main__':
    unittest.main()