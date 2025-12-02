def sum_even_and_even_index(arr):
    if not arr or not all(isinstance(i, (int, float)) for i in arr):
        return "Invalid input. Please provide a non-empty list containing only numeric values."

    even_sum = 0
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 == 0:
            even_sum += arr[i]

    return even_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_even_and_even_index([5, 6, 12, 1, 18, 8]), 30)

if __name__ == '__main__':
    unittest.main()