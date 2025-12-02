def find_first_occurrence(A, x):
    if not A:
        return -1
    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left if A[left] == x else -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5), 1)

if __name__ == '__main__':
    unittest.main()