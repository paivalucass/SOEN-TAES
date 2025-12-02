def is_Monotonic(A):
    if not isinstance(A, list) or len(A) == 0:
        raise ValueError("Input should be a non-empty array")

    def is_monotonic_increasing(arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    def is_monotonic_decreasing(arr):
        return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

    is_increasing_result = is_monotonic_increasing(A)
    is_decreasing_result = is_monotonic_decreasing(A)

    return is_increasing_result or is_decreasing_result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Monotonic([6, 5, 4, 4]), True)

if __name__ == '__main__':
    unittest.main()