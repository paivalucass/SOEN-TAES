def jacobsthal_num(n):
    # Function to find the nth Jacobsthal number
    # Using the mathematical algorithm and logic described in the provided link
    # Input validation
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    # Implementing error handling for large numbers
    if n > 93:  # Jacobsthal numbers exceed the limit for integers after n = 93
        raise ValueError("Input value too large")

    # Calculating the Jacobsthal number using the iterative approach
    a, b = 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(2, n + 1):
            c = b + 2 * a
            a, b = b, c
        return c
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(jacobsthal_num(5), 11)

if __name__ == '__main__':
    unittest.main()