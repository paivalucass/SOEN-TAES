def is_min_heap(arr, i):
    n = len(arr)
    if i >= n:
        return True
    left = 2 * i + 1
    right = 2 * i + 2
    if (left < n and arr[i] > arr[left]) or (right < n and arr[i] > arr[right]):
        return False
    return is_min_heap(arr, left) and is_min_heap(arr, right)

# test function

def check_min_heap(arr):
    return is_min_heap(arr, 0)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_min_heap([1, 2, 3, 4, 5, 6]), True)

if __name__ == '__main__':
    unittest.main()