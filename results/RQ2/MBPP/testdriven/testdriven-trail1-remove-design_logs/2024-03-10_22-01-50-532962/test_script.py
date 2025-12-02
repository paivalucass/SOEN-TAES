def get_total_number_of_sequences(m, n):
    if n == 0:
        return 1
    if n == 1:
        return m
    if m < 2:
        return 0
    dp = [0] * (m + 1)
    dp[1] = m
    for i in range(2, n + 1):
        new_dp = [0] * (m + 1)
        for j in range(1, m + 1):
            for k in range(j * 2, m + 1):
                new_dp[k] += dp[j]
        dp = new_dp
    return sum(dp)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_total_number_of_sequences(10, 4), 4)

if __name__ == '__main__':
    unittest.main()