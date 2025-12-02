def sum_div(number):
    divisor_sum = 0
    if number <= 0:
        return 0
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisor_sum += i
            if i != number // i:
                divisor_sum += number // i
    return divisor_sum - number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_div(8), 7)

if __name__ == '__main__':
    unittest.main()