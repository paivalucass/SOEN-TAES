def find_remainder(arr, n):
    if len(arr) == 0 or n == 0:
        return "Invalid input: The input array cannot be empty and n cannot be 0."

    product = 1
    for num in arr:
        product *= num

    remainder = product % n
    return remainder
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_remainder([100, 10, 5, 25, 35, 14], 11), 9)

if __name__ == '__main__':
    unittest.main()