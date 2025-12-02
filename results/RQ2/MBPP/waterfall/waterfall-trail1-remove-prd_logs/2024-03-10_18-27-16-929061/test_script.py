def sequence(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    memo = [0, 1, 1]
    if n <= 2:
        return memo[n]

    for i in range(3, n + 1):
        memo.append(memo[memo[i - 1]] + memo[i - memo[i - 1]])

    return memo[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequence(10), 6)

if __name__ == '__main__':
    unittest.main()