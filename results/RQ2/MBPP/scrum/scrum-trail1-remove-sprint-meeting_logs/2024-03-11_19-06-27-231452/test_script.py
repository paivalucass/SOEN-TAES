def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if int(left_half[i]) < int(right_half[j]):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def sort_numeric_strings(nums_str):
    nums_str = [int(num) for num in nums_str]
    merge_sort(nums_str)
    return nums_str
import unittest

class Test(unittest.TestCase):
    def test_sort_numeric_strings(self):
        self.assertEqual(sort_numeric_strings(['4', '12', '45', '7', '0', '100', '200', '-12', '-500']), [-500, -12, 0, 4, 7, 12, 45, 100, 200])

if __name__ == '__main__':
    unittest.main()