def eulerian_num(n, m): 
    memoization = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

    def calculate_eulerian_num_recursive(n, m):
        if memoization[n][m] != -1:
            return memoization[n][m]
        if n == 0:
            return 1 if m == 0 else 0
        if m == 0:
            return 0
        result = (m + 1) * calculate_eulerian_num_recursive(n - 1, m) + (n - m) * calculate_eulerian_num_recursive(n - 1, m - 1)
        memoization[n][m] = result
        return result

    return calculate_eulerian_num_recursive(n, m)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(eulerian_num(3, 1), 4)

if __name__ == '__main__':
    unittest.main()