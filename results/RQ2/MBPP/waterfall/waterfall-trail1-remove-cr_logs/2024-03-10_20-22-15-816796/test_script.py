def find_max_difference(binary_string):
    if not isinstance(binary_string, str) or set(binary_string) - {'0', '1'}:
        raise ValueError("Input is not a valid binary string")

    max_difference = 0
    current_difference = 0
    count_of_zeros = 0
    count_of_ones = 0

    for char in binary_string:
        if char == '0':
            count_of_zeros += 1
        else:
            count_of_ones += 1
        current_difference = count_of_zeros - count_of_ones
        max_difference = max(max_difference, abs(current_difference))

    return max_difference
import unittest

class Test(unittest.TestCase):
    def test_find_length(self):
        self.assertEqual(find_length('11000010001'), 6)

if __name__ == '__main__':
    unittest.main()