def median_numbers(a, b, c):
    try:
        input_list = [a, b, c]
        if len(input_list) != len(set(input_list)):
            return "Error: Input includes duplicate numbers"
        sorted_list = sorted(input_list)
        if any(num < 0 for num in sorted_list):
            return "Error: Input includes negative numbers"
        if len(sorted_list) % 2 == 0:
            return (sorted_list[len(sorted_list) // 2 - 1] + sorted_list[len(sorted_list) // 2]) / 2
        else:
            return sorted_list[len(sorted_list) // 2]
    except TypeError:
        return "Error: Invalid input"

# Test cases
print(median_numbers(25, 55, 65)) # Expected output: 55.0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_numbers(25, 55, 65), 55.0)

if __name__ == '__main__':
    unittest.main()