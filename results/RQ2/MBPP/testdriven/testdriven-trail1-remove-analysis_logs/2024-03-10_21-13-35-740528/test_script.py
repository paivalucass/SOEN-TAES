def max_sum(arr): 
    n = len(arr)
    if n == 0:
        return 0
    inc = [0] * n
    dec = [0] * n
    inc[0] = arr[0]
    dec[n-1] = arr[n-1]

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            inc[i] = inc[i-1] + arr[i]
        else:
            inc[i] = arr[i]

    for i in range(n-2, 0, -1):
        if arr[i] > arr[i+1]:
            dec[i] = dec[i+1] + arr[i]
        else:
            dec[i] = arr[i]

    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - arr[i])

    return max_sum
import unittest

class Test(unittest.TestCase):
    def test_max_sum(self):
        self.assertEqual(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]), 194)

if __name__ == '__main__':
    unittest.main()