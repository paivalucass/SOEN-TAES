def sum_div(number):
    if number <= 0:
        return 0
    divisors_sum = 1
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            divisors_sum += i
    return divisors_sum
import unittest

class Test(unittest.TestCase):
    def test_sum_div(self):
        self.assertEqual(sum_div(8), 7)

if __name__ == '__main__':
    unittest.main()