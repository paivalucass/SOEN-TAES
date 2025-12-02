def amicable_numbers_sum(limit):
    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("Input parameter must be a positive integer")

    def get_divisors_sum(number):
        divisors_sum = 0
        for i in range(1, number):
            if number % i == 0:
                divisors_sum += i
        return divisors_sum

    def is_amicable_pair(num1, num2):
        return num1 != num2 and get_divisors_sum(num1) == num2 and get_divisors_sum(num2) == num1

    def calculate_amicable_sum(limit):
        amicable_sum = 0
        for num in range(1, limit):
            pair = get_divisors_sum(num)
            if is_amicable_pair(num, pair):
                amicable_sum += num
        return amicable_sum

    return calculate_amicable_sum(limit)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(amicable_numbers_sum(999), 504)

if __name__ == '__main__':
    unittest.main()