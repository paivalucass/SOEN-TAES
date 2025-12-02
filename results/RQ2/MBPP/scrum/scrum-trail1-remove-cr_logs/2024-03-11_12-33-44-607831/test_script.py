def bell_number(n):
    if n < 0 or not isinstance(n, int):
        raise ValueError("Input parameter 'n' must be a non-negative integer")

    bell = [0] * (n + 1)
    bell[0] = 1
    for i in range(1, n + 1):
        bell[i] = 0
        for j in range(i):
            bell[i] += bell[j] * (i - j)

    return bell[n]
import unittest

class Test(unittest.TestCase):
    def test_bell_number(self):
        self.assertEqual(bell_number(2), 2)

if __name__ == '__main__':
    unittest.main()