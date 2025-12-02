def odd_length_sum(arr):
    sum = 0
    n = len(arr)
    for i in range(n):
        for j in range(i, n, 2):
            for k in range(i, j+1):
                sum += arr[k]
    return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_length_sum([1, 2, 4]), 14)

if __name__ == '__main__':
    unittest.main()