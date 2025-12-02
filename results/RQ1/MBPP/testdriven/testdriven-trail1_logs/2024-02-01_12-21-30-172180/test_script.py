def division_elements(test_tup1, test_tup2):
    '''
    Write a function that takes in two tuples and performs mathematical division operation element-wise across the given tuples.
    assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
    '''

    # Input validation to ensure that the input tuples are of the same length
    if len(test_tup1) != len(test_tup2) or 0 in test_tup2:
        raise ValueError("Input tuples must be of the same length and cannot contain zero")

    # Perform mathematical division operation element-wise across the given tuples
    result = tuple(x / y for x, y in zip(test_tup1, test_tup2))

    return result

# Add comments to explain the purpose of input validation and mathematical division operation
# Include test cases to cover scenarios such as division by zero, negative numbers, and edge cases.
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(division_elements((10, 4, 6, 9),(5, 2, 3, 3)), (2, 2, 2, 3))

if __name__ == '__main__':
    unittest.main()