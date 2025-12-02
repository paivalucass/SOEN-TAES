def check_min_heap(arr):
    n = len(arr)
    for i in range((n // 2) - 1, -1, -1):
        if arr[i] > arr[(2 * i) + 1] or ((2 * i) + 2 < n and arr[i] > arr[(2 * i) + 2]):
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_min_heap([1, 2, 3, 4, 5, 6]), True)

if __name__ == '__main__':
    unittest.main()