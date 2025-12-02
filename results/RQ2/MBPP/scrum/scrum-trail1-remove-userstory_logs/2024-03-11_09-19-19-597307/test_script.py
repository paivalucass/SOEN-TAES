def bell_Number(n):
    if n < 0:
        raise ValueError("Input n should be a non-negative integer")

    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1

    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]

        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]

    return bell[n][0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bell_Number(2), 2)

if __name__ == '__main__':
    unittest.main()