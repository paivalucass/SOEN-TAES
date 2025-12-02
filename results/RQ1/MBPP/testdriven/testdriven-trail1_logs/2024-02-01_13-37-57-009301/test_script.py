def odd_length_sum(arr):
    total_sum = 0
    n = len(arr)
    for i in range(n):
        total_sum += (((i + 1) * (n - i) + 1) // 2) * arr[i]
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_length_sum([1,2,4]), 14)

if __name__ == '__main__':
    unittest.main()