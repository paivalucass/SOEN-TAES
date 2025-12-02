def find_solution(a, b, n):
    if not all(isinstance(i, int) for i in [a, b, n]) or a == 0 or b == 0 or n == 0:
        return None

    def extended_gcd(a, b):
        if b == 0:
            return (1, 0)
        else:
            x, y = extended_gcd(b, a % b)
            return (y, x - (a // b) * y)

    g = extended_gcd(a, b)
    if n % g[0] != 0:
        return None

    x = g[0] * (n // g[0])
    y = g[1] * (n // g[0])
    return (x, y)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_solution(2, 3, 7), (2, 1))

if __name__ == '__main__':
    unittest.main()