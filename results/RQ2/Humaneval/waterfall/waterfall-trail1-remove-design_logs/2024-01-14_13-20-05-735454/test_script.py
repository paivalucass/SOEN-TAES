def special_factorial(n):
    if n < 1:
        return "Invalid input"
    if n == 1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= factorial_helper(i)
    return result

def factorial_helper(n):
    if n == 1:
        return 1
    return n * factorial_helper(n-1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(special_factorial(4), 288)

if __name__ == '__main__':
    unittest.main()