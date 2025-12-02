def max_sub_array_sum_repeated(a, n, k):
    max_sum = float('-inf')
    current_sum = 0
    for _ in range(k):
        for i in range(n):
            current_sum = max(a[i], current_sum + a[i])
            max_sum = max(max_sum, current_sum)
    return max_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3), 30)

if __name__ == '__main__':
    unittest.main()