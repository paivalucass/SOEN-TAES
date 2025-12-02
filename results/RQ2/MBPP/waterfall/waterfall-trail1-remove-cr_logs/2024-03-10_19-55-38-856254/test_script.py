def are_equivalent(num1, num2):
    return sum_of_divisors(num1) == sum_of_divisors(num2)


def sum_of_divisors(n):
    div_sum = 0
    for i in range(1, n):
        if n % i == 0:
            div_sum += i
    return div_sum


def div_sum(n):
    return sum_of_divisors(n)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(div_sum(36, 57), False)

if __name__ == '__main__':
    unittest.main()