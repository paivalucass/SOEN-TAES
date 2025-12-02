def special_factorial(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"

    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    def special_factorial_recursive(n):
        if n == 1:
            return factorial(1)
        return factorial(n) * special_factorial_recursive(n - 1)

    return special_factorial_recursive(n)
import unittest


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(special_factorial(4), 288)

if __name__ == '__main__':
    unittest.main()