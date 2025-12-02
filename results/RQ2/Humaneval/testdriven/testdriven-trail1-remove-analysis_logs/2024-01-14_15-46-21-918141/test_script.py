def get_positive(l: list):
    """Return only positive numbers in the list."""
    if not isinstance(l, list):
        raise TypeError("Input parameter must be a list")
    
    result = [num for num in l if num > 0]
    return result

# Test the function with various inputs
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123, 1]
import unittest

class Test(unittest.TestCase):
    def test_get_positive(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

if __name__ == '__main__':
    unittest.main()