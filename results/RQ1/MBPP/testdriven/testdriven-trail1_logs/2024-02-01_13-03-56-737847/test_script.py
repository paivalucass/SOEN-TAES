def find_kth(arr1, arr2, k):
    '''Write a function to find kth element from the given two sorted arrays.'''
    i = 0
    j = 0
    while True:
        if i == len(arr1):
            return arr2[j + k - 1]
        if j == len(arr2):
            return arr1[i + k - 1]
        if k == 1:
            return min(arr1[i], arr2[j])
        
        new_i = min(i + k//2, len(arr1)) - 1
        new_j = min(j + k//2, len(arr2)) - 1
        
        if arr1[new_i] <= arr2[new_j]:
            k -= new_i - i + 1
            i = new_i + 1
        else:
            k -= new_j - j + 1
            j = new_j + 1
          
# Test case
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5), 6)

if __name__ == '__main__':
    unittest.main()