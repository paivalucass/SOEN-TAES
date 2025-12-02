def find_kth(arr1, arr2, k):
    if k < 1 or k > len(arr1) + len(arr2):
        return None
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    if not arr1:
        return arr2[k - 1]
    if not arr2:
        return arr1[k - 1]
    if k == 1:
        return min(arr1[0], arr2[0])
    idx1 = min(k // 2, len(arr1))
    idx2 = k - idx1
    if arr1[idx1 - 1] < arr2[idx2 - 1]:
        return find_kth(arr1[idx1:], arr2, k - idx1)
    else:
        return find_kth(arr1, arr2[idx2:], k - idx2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5), 6)

if __name__ == '__main__':
    unittest.main()