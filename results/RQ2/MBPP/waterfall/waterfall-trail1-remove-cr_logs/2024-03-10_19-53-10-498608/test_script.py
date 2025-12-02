def count(lst):
    count = 0
    if isinstance(lst, list):
        for item in lst:
            if item == True:
                count += 1
        return count
    else:
        raise TypeError("Input must be a list")
        return -1 # Return -1 for invalid input

# Additional input validation for empty list
assert count([]) == 0
# Performance optimization for handling large lists efficiently
# No additional code needed, as the iteration through the list is already efficient.
import unittest

class Test(unittest.TestCase):
    def test_count_true_booleans(self):
        self.assertEqual(count([True, False, True]), 2)

if __name__ == '__main__':
    unittest.main()