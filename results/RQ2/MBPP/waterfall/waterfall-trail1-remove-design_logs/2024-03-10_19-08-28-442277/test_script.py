def div_sum(num1, num2):
    def sum_of_divisors(num):
        divisors_sum = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divisors_sum += i
                if i != num // i:
                    divisors_sum += num // i
        return divisors_sum

    return sum_of_divisors(num1) == sum_of_divisors(num2)
import unittest

class Test(unittest.TestCase):
    def test_div_sum(self):
        self.assertEqual(div_sum(36, 57), False)

if __name__ == '__main__':
    unittest.main()