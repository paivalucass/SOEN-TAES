def max_sub_array_sum_repeated(a, n, k):
    max_sum = float('-inf')
    for i in range(n):
        curr_sum = 0
        for j in range(i, i + n * k):
            curr_sum += a[j % n]
            max_sum = max(max_sum, curr_sum)
    return max_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3), 30)

if __name__ == '__main__':
    unittest.main()