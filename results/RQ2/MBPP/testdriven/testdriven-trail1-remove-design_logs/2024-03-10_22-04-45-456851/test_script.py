def sum_div(number):
    '''
    Write a function to return the sum of all divisors of a number.
    assert sum_div(8)==7
    '''
    if not isinstance(number, (int, float)):
        return 0
    if number <= 0:
        return 0

    divisors_sum = 1  # 1 is always a divisor
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:
                divisors_sum += number // i

    return divisors_sum
import unittest

class Test(unittest.TestCase):
    def test_sum_div(self):
        self.assertEqual(sum_div(8), 7)

if __name__ == '__main__':
    unittest.main()