def are_equivalent(n1, n2):
    def sum_of_divisors(x):
        div_sum = 1
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                div_sum += i
                if i != x // i:
                    div_sum += x // i
        return div_sum

    a = sum_of_divisors(n1)
    b = sum_of_divisors(n2)
    return a == b

assert are_equivalent(36, 57) == False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(are_equivalent(36, 57), False)

if __name__ == '__main__':
    unittest.main()