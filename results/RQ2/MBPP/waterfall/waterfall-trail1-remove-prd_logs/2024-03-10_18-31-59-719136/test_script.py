def max_sum(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    n = len(arr)
    lis = [0] * n
    lds = [0] * n
    max_sum = 0
    
    for i in range(n):
        lis[i] = arr[i]
        lds[i] = arr[i]
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + arr[i]:
                lis[i] = lis[j] + arr[i]
    
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j] and lds[i] < lds[j] + arr[i]:
                lds[i] = lds[j] + arr[i]
    
    for i in range(n):
        max_sum = max(max_sum, lis[i] + lds[i] - arr[i])
    
    return max_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]), 194)

if __name__ == '__main__':
    unittest.main()