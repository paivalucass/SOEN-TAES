def special_factorial(n):
    if n <= 0:
        return None
    result = 1
    while n > 0:
        result *= factorial(n)
        n -= 1
    return result


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(special_factorial(4), 288)
        self.assertEqual(special_factorial(1), 1)
        self.assertEqual(special_factorial(2), 2)
        self.assertEqual(special_factorial(3), 12)
        self.assertEqual(special_factorial(5), 34560)

if __name__ == '__main__':
    unittest.main()