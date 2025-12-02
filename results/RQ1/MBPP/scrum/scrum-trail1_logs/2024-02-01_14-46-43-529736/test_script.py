def find_solution(a, b, n):
    def gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x
    if n % gcd(a, b) == 0:
        (x, y) = (0, 0)
        while x * a <= n:
            if (n - x * a) % b == 0:
                y = (n - x * a) // b
                return (x, y)
            x += 1
        return None
    else:
        return None

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_solution(2, 3, 7), (2, 1))

if __name__ == '__main__':
    unittest.main()