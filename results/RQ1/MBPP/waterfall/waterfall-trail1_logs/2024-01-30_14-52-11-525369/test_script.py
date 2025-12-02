def get_median(arr1, arr2, n):
    if len(arr1) != len(arr2):
        raise ValueError("Input lists must be of the same size")
    if len(arr1) == 0:
        raise ValueError("Input lists cannot be empty")
    
    merged_list = merge_sorted(arr1, arr2)
    if n % 2 == 0:
        return (merged_list[n//2] + merged_list[n//2 - 1]) / 2
    else:
        return merged_list[n//2]

def merge_sorted(arr1, arr2):
    result = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result += arr1[i:]
    result += arr2[j:]
    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5), 16.0)

if __name__ == '__main__':
    unittest.main()