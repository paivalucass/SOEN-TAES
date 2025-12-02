def find_kth(arr1, arr2, k):
    i, j, count = 0, 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            count += 1
            if count == k:
                return arr1[i]
            i += 1
        else:
            count += 1
            if count == k:
                return arr2[j]
            j += 1
    while i < len(arr1):
        count += 1
        if count == k:
            return arr1[i]
        i += 1
    while j < len(arr2):
        count += 1
        if count == k:
            return arr2[j]
        j += 1
    return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5), 6)

if __name__ == '__main__':
    unittest.main()