def find_kth(arr1, arr2, k):
    # Merge arr1 and arr2
    merged_arr = merge(arr1, arr2)

    # Handle edge cases
    if len(merged_arr) == 0:
        return "Error: Empty arrays"
    if k < 1 or k > len(merged_arr):
        return "Error: k value out of bounds"
    
    # Return the kth element from the merged and sorted version of arr1 and arr2
    return merged_arr[k - 1]

def merge(arr1, arr2):
    i = 0
    j = 0
    merged_arr = []

    # Merge arr1 and arr2 into a single sorted array
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1

    return merged_arr

# Test Cases:
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5), 6)

if __name__ == '__main__':
    unittest.main()