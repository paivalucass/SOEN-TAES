def check_min_heap_helper(arr, i):
    n = len(arr)
    if i >= n // 2:
        return True
    if arr[i] > arr[2 * i + 1] or (2 * i + 2 < n and arr[i] > arr[2 * i + 2]):
        return False
    return (check_min_heap_helper(arr, 2 * i + 1) and check_min_heap_helper(arr, 2 * i + 2))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_min_heap_helper([1, 2, 3, 4, 5, 6], 0), True)

if __name__ == '__main__':
    unittest.main()