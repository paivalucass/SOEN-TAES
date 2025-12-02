def odd_Equivalent(s, n):
    # check if the input binary string 's' is valid (contains only 0s and 1s)
    if not all(char in '01' for char in s):
        raise ValueError("Input binary string contains invalid characters")

    # Check if the number 'n' is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input number 'n' must be a non-negative integer")

    # Apply rotation logic to rotate the binary string 's' the given number of times
    rotated_string = s[-n:] + s[:-n]

    # Count the number of numbers with an odd value in the rotated string
    count = sum([1 for char in rotated_string if char == '1'])

    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_Equivalent("011001", 6), 3)

if __name__ == '__main__':
    unittest.main()