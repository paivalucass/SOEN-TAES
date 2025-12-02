def check_min_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_min_heap([1, 2, 3, 4, 5, 6]), True)

if __name__ == '__main__':
    unittest.main()