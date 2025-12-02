def get_Inv_Count(arr):
    inv_count = 0
    if len(arr) <= 1:
        return inv_count
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    inv_count += get_Inv_Count(left)
    inv_count += get_Inv_Count(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            inv_count += (mid - i)
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return inv_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Inv_Count([1,20,6,4,5]), 5)

if __name__ == '__main__':
    unittest.main()