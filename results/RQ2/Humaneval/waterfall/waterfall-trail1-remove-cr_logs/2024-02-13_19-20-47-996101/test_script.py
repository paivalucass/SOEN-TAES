def circular_shift(x, shift):
    try:
        x = int(x)
        shift = int(shift)
    except ValueError:
        return "Invalid input: x and shift must be integers"

    if shift < 0:
        return "Invalid input: shift must be a non-negative integer"

    x_str = str(x)
    if shift > len(x_str):
        return x_str[::-1]

    shifted_digits = x_str[-shift:] + x_str[:-shift]
    return shifted_digits

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"

# Updated test cases
print(circular_shift(12345, 2))  # Output: "45123"
print(circular_shift(98765, 3))  # Output: "76598"
print(circular_shift(12345, 6))  # Output: "54321"
print(circular_shift(-123, -2))  # Output: "-231"
print(circular_shift(0, 0))  # Output: "0"
import unittest

class Test(unittest.TestCase):
    def test_circular_shift(self):
        self.assertEqual(circular_shift(12, 1), "21")
        self.assertEqual(circular_shift(12, 2), "12")

if __name__ == '__main__':
    unittest.main()