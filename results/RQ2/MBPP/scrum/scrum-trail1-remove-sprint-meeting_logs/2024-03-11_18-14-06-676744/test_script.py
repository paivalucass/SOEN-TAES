def bell_number(n):
    memo = {0: 1, 1: 1}

    for i in range(2, n+1):
        memo[i] = 0
        for j in range(i):
            memo[i] += memo[j] * memo[i-j-1]

    return memo[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bell_number(2), 2)

if __name__ == '__main__':
    unittest.main()