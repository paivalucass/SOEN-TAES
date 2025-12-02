def find_remainder(arr, n):
    if not isinstance(arr, list) or not isinstance(n, int) or n <= 0:
        return "Input is invalid"  # Input validation
    if n == 0:
        return "n cannot be 0"
    product = 1
    for num in arr:
        product = (product * num) % n
    return product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_remainder([100, 10, 5, 25, 35, 14], 11), 9)

if __name__ == '__main__':
    unittest.main()