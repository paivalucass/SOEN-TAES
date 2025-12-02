def max_product(arr):
    if len(arr) < 2:
        return 0
    max_result = 0
    current_product = 1
    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            current_product *= arr[i]
        else:
            max_result = max(max_result, current_product)
            current_product = 1
    max_result = max(max_result, current_product)
    return max_result
import unittest

class Test(unittest.TestCase):
    def test_max_product(self):
        self.assertEqual(max_product([3, 100, 4, 5, 150, 6]), 3000)

if __name__ == '__main__':
    unittest.main()