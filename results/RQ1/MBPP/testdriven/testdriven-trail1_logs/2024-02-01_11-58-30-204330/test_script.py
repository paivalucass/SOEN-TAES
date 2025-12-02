def closest_num(N):
    '''Write a function to find the closest smaller number than n.'''
    if N >= 0:
        return N - 1
    else:
        return N - 1
    # Handle negative numbers and edge cases appropriately
    # Use assert statements to validate the function output against the expected output for each test case
    # Provide detailed comments explaining the logic and approach used in the function
    # Write a function to find the closest smaller number than n.
    # assert closest_num(11) == 10
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_num(11), 10)

if __name__ == '__main__':
    unittest.main()