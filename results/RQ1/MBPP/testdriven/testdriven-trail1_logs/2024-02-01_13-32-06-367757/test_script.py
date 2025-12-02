def _sum(arr):
    '''
    This Python function calculates the sum of the elements in the input array.

    Args:
    arr (list): Input array containing integers or floating point numbers.

    Returns:
    float: The sum of all elements in the array.

    Raises:
    TypeError: If the input is not a list.
    ValueError: If the input list is empty.
    '''
    # Validate input array
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")

    # Calculate sum
    result = sum(arr)

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(_sum([1, 2, 3]), 6)

if __name__ == '__main__':
    unittest.main()