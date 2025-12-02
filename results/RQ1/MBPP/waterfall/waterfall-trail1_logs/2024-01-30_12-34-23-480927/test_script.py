def find_maximum_difference_between_zeros_and_ones(binary_string):
    if not binary_string:
        return 0

    max_difference = 0
    current_difference = 0

    for char in binary_string:
        if char == '0':
            current_difference += 1
        else:
            current_difference -= 1

        max_difference = max(max_difference, current_difference)

        if current_difference < 0:
            current_difference = 0

    return max_difference

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_length('11000010001'), 6)

if __name__ == '__main__':
    unittest.main()