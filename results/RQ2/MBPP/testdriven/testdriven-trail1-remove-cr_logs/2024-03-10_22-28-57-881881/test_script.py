def is_Diff(n):
    '''Write a python function to find whether a number is divisible by 11.'''
    # Input validation to ensure 'n' is an integer
    if isinstance(n, int):
        # Check if the number is divisible by 11
        if n < 0:
            n = abs(n)
        return n % 11 == 0
    else:
        # Handle non-integer input
        raise ValueError("Input must be an integer")

# Example test case
assert is_Diff(12345) == False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Diff(12345), False)

if __name__ == '__main__':
    unittest.main()