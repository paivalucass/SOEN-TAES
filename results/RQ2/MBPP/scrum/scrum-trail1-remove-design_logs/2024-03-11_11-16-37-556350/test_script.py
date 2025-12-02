def odd_length_sum(arr):
    result = 0
    n = len(arr)
    for i in range(n):
        odd = 0
        even = 0
        for j in range(i, n):
            if (j - i + 1) % 2 == 1:
                for k in range(i, j + 1):
                    result += arr[k]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_length_sum([1,2,4]), 14)

if __name__ == '__main__':
    unittest.main()