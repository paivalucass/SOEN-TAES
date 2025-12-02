def get_total_number_of_sequences(m, n):
    if not (isinstance(m, int) and isinstance(n, int) and m > 0 and n > 0):
        return "Invalid input"

    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(j//2, j+1):
                dp[i][j] += dp[i-1][k]

    return sum(dp[n])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_total_number_of_sequences(10, 4), 4)

if __name__ == '__main__':
    unittest.main()