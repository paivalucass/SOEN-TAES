def add_elements(arr, k):
    if not isinstance(arr, list):
        raise ValueError("Input arr must be a list of integers")

    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements of arr must be integers")

    if not (1 <= k <= len(arr)):
        raise ValueError("Invalid value of k")

    filtered_elements = [x for x in arr[:k] if abs(x) < 100]

    result = sum(filtered_elements)

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_elements([111,21,3,4000,5,6,7,8,9], 4), 24)

if __name__ == '__main__':
    unittest.main()