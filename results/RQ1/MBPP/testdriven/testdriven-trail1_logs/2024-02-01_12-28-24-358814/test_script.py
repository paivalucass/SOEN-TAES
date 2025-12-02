def count_no_of_ways(n, k):
    if not isinstance(n, int) or not isinstance(k, int) or n <= 0 or k <= 0:
        raise ValueError("Invalid input parameters. Please enter positive integers for n and k.")
    # Input validation to ensure that n and k are positive integers
    if n <= 0 or k <= 0:
        return 0
    if n == 1:
        return k
    same = 0
    diff = k
    for i in range(2, n+1):
        temp = diff
        diff = (same + diff) * (k-1)
        same = temp
    return same + diff

# Utilize dynamic programming to optimize the calculation of the number of ways
# Memoization can be used to store the results of subproblems
# Your implementation details here
# Placeholder for the actual code to calculate the number of ways
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_no_of_ways(2, 4), 16)

if __name__ == '__main__':
    unittest.main()