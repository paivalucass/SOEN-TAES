def get_Inv_Count(arr):
    if not isinstance(arr, list):
        raise TypeError("Input should be a list")
    inv_count = 0
    if len(arr) <= 1:
        return inv_count, arr

    def mergeAndCountInversions(left_arr, right_arr):
        inv_count = 0
        merged_arr = []
        i, j = 0, 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                merged_arr.append(left_arr[i])
                i += 1
            else:
                merged_arr.append(right_arr[j])
                j += 1
                inv_count += (len(left_arr) - i)
        merged_arr += left_arr[i:]
        merged_arr += right_arr[j:]

        return inv_count, merged_arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    inv_count_left, sorted_left_arr = get_Inv_Count(left_arr)
    inv_count_right, sorted_right_arr = get_Inv_Count(right_arr)
    inv_count_merge, merged_arr = mergeAndCountInversions(sorted_left_arr, sorted_right_arr)

    inv_count = inv_count_left + inv_count_right + inv_count_merge
    return inv_count, merged_arr
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Inv_Count([1,20,6,4,5]), 5)

if __name__ == '__main__':
    unittest.main()