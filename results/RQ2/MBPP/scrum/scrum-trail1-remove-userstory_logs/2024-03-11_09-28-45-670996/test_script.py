def right_insertion(a, x):
    if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
        raise ValueError("Input array 'a' is not sorted")
    
    if not a:
        return 0
    
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(right_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()