def square_nums(nums):
    squared_numbers = [num ** 2 for num in nums]
    return squared_numbers

# Test cases
print(square_nums([]))  # Expected output: []
print(square_nums([1, 2, 3, 4]))  # Expected output: [1, 4, 9, 16]
print(square_nums([-1, -2, -3, -4]))  # Expected output: [1, 4, 9, 16]
print(square_nums([0]))  # Expected output: [0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

if __name__ == '__main__':
    unittest.main()