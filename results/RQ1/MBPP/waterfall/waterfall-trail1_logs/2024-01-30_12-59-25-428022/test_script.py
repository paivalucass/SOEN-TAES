def sum_div(number):
    divisors_sum = 1
    sqrt_num = int(number**0.5)
    for i in range(2, sqrt_num+1):
        if number % i == 0:
            divisors_sum += i
            if i != number//i:
                divisors_sum += number//i
    return divisors_sum
import unittest

class Test(unittest.TestCase):
    def test_sum_div(self):
        self.assertEqual(sum_div(8), 7)

if __name__ == '__main__':
    unittest.main()