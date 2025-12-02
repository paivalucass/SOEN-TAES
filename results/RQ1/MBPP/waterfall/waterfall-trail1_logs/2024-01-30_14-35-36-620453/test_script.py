def find_remainder(arr, n):
    if not arr:
        return "Error: Input array is empty, please provide valid input"
    if n <= 0:
        return "Error: Invalid value for n, it should be greater than 0"

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