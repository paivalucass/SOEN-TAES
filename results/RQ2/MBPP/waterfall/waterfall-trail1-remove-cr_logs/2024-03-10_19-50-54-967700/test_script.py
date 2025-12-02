def bell_number(n):
    if not isinstance(n, int) or n < 0:
        return "Invalid input"
    bell = [0] * (n + 1)
    bell[0] = 1
    for i in range(1, n + 1):
        bell[i] = 0
        for j in range(i):
            bell[i] += bell[j] * binomialCoefficient(i - 1, j)
    return bell[n]

def binomialCoefficient(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bell_number(2), 2)

if __name__ == '__main__':
    unittest.main()