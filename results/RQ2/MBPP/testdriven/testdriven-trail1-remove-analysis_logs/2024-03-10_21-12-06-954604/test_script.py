def are_equivalent(num1, num2):
    return sum_of_divisors(num1) == sum_of_divisors(num2)


def sum_of_divisors(num):
    if num == 0:
        return 0
    div_sum = 0
    for i in range(1, num):
        if num % i == 0:
            div_sum += i
    return div_sum

def div_sum(n1, n2):
    return sum_of_divisors(n1) == sum_of_divisors(n2)

# Test the function with the provided test case
assert are_equivalent(36, 57) == False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(div_sum(36, 57), False)

if __name__ == '__main__':
    unittest.main()