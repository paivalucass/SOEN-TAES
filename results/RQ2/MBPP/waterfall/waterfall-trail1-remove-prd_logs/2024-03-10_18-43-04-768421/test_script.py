def find_kth(arr1, arr2, k):
    if not arr1 or not arr2:
        raise ValueError("Input arrays cannot be empty")
    if k < 1 or k > len(arr1) + len(arr2):
        raise ValueError("k is out of range")

    merged_array = merge_sorted_arrays(arr1, arr2)
    if k == len(merged_array):
        raise ValueError("k is equal to the length of the merged array")
    return merged_array[k-1]


def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged += arr1[i:]
    merged += arr2[j:]
    return merged

def test_find_kth():
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6


test_find_kth()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5), 6)

if __name__ == '__main__':
    unittest.main()