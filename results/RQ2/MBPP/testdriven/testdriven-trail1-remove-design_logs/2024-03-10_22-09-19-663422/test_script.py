def sum_of_even_factors(number):
    result = 0
    for i in range(1, number + 1):
        if number % i == 0 and i % 2 == 0:
            result += i
    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sumofFactors(18), 26)

if __name__ == '__main__':
    unittest.main()