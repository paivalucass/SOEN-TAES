def binomial_coefficient(n, k):
    if not isinstance(n, int) or not isinstance(k, int) or n < 0 or k < 0:
        return "Invalid input"
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1

    result = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)

    return result

# Test Script

def test_binomial_coefficient():
    assert binomial_coefficient(3, 2) == 3
    assert binomial_coefficient(8, 3) == 56
    assert binomial_coefficient(5, 2) == 10
    assert binomial_coefficient(10, 5) == 252

# Run the test

test_binomial_coefficient()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(binomial_Coeff(3, 2), 3)  # Replace with the actual output value

if __name__ == '__main__':
    unittest.main()