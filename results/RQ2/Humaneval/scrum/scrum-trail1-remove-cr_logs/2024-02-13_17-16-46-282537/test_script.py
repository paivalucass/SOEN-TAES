def special_factorial(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid Input Error"
    result = 1
    for i in range(n, 0, -1):
        factorial = 1
        for j in range(i, 0, -1):
            factorial *= j
        result *= factorial
    return result
import unittest

class Test(unittest.TestCase):
    def test_special_factorial(self):
        self.assertEqual(special_factorial(4), 288)

if __name__ == '__main__':
    unittest.main()