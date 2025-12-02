def get_median(arr1, arr2, n):
    if len(arr1) != len(arr2) or n != len(arr1):
        return "Error: Lists are not of the same size or incorrect input size"
    
    for i in range(n-1):
        if arr1[i] > arr1[i+1] or arr2[i] > arr2[i+1]:
            return "Error: Lists are not sorted"
    
    merged = sorted(arr1 + arr2)
    mid = len(merged) // 2
    
    if len(merged) % 2 == 0:
        return (merged[mid-1] + merged[mid]) / 2
    else:
        return merged[mid]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5), 16.0)

if __name__ == '__main__':
    unittest.main()