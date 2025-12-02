def find_remainder(arr, n):
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        raise ValueError("Input array must be a list of integers")
    if not arr or n == 0:
        raise ValueError("Input array cannot be empty and n cannot be 0")

    product = 1
    for num in arr:
        product *= num

    return product % n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_remainder([100, 10, 5, 25, 35, 14], 11), 9)

if __name__ == '__main__':
    unittest.main()