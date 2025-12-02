def find_kth(arr1, arr2, k):
    '''Write a function to find kth element from the given two sorted arrays.'''
    if not arr1:
        return arr2[k - 1]
    elif not arr2:
        return arr1[k - 1]
    else:
        if k == 1:
            return min(arr1[0], arr2[0])
        i, j = 0, 0
        while True:
            if i == len(arr1):
                return arr2[j + k - 1]
            if j == len(arr2):
                return arr1[i + k - 1]
            if k == 1:
                return min(arr1[i], arr2[j])
            new_i = min(i + k // 2, len(arr1))
            new_j = min(j + k // 2, len(arr2))
            if arr1[new_i - 1] <= arr2[new_j - 1]:
                k -= new_i - i
                i = new_i
            else:
                k -= new_j - j
                j = new_j

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5), 6)

if __name__ == '__main__':
    unittest.main()