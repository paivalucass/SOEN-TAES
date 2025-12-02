def check_min_heap_helper(arr, i):
    n = len(arr)
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] < arr[i]:
        return False
    if right < n and arr[right] < arr[i]:
        return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_min_heap_helper([1, 2, 3, 4, 5, 6], 0), True)

if __name__ == '__main__':
    unittest.main()