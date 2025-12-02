def greatest_common_divisor(a: int, b: int) -> int:
    a_factors = calculate_factors(a)
    b_factors = calculate_factors(b)
    common_factors = find_common_factors(a_factors, b_factors)
    return max(common_factors) if common_factors else 1

def calculate_factors(num: int):
    factors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num // i)
    return factors

def find_common_factors(a_factors, b_factors):
    return list(set(a_factors) & set(b_factors))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)

if __name__ == '__main__':
    unittest.main()