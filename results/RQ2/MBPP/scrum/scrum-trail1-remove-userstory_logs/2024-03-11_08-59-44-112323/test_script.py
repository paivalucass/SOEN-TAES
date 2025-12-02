def get_total_number_of_sequences(m, n):
    if not isinstance(m, int) or not isinstance(n, int) or m <= 0 or n <= 0:
        return "Invalid input: m and n must be positive integers"
    
    memo = {}

    def helper(prev, length):
        if length == 0:
            return 1
        if (prev, length) in memo:
            return memo[(prev, length)]

        total = 0
        for i in range(prev * 2, m + 1):
            total += helper(i, length - 1)
        memo[(prev, length)] = total
        return total

    return helper(1, n - 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_total_number_of_sequences(10, 4), 4)

if __name__ == '__main__':
    unittest.main()