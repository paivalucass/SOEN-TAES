def eulerian_num(n, m):
    if n < 0 or m < 0:
        return None
    if n == 0:
        return None

    a = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                a[i][j] = 1
            elif j == 0:
                a[i][j] = 0
            else:
                a[i][j] = (i - j) * a[i - 1][j] + (j + 1) * a[i - 1][j - 1]

    return a[n][m]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(eulerian_num(3, 1), 4)

if __name__ == '__main__':
    unittest.main()