def odd_length_sum(arr):
    result = 0
    n = len(arr)
    for i in range(n):
        result += ((i + 1) * (n - i) + 1) // 2 * arr[i]
    return result
import unittest

class Test(unittest.TestCase):
    def test_odd_length_sum(self):
        self.assertEqual(odd_length_sum([1,2,4]), 14)

if __name__ == '__main__':
    unittest.main()