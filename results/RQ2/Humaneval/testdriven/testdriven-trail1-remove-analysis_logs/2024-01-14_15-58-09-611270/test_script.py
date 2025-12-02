def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """

    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input should be a list")
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements in the list should be integers")

    # Edge case for empty list
    if not arr:
        return None

    # Initialize variables
    product_of_signs = 1
    sum_of_magnitudes = 0

    # Calculate product of signs and sum of magnitudes
    for num in arr:
        if num > 0:
            sum_of_magnitudes += num
        else:
            sum_of_magnitudes -= num
        
        if num == 0:
            sign = 0
        elif num > 0:
            sign = 1
        else:
            sign = -1
        
        product_of_signs *= sign
    
    # Return the result
    return sum_of_magnitudes * product_of_signs
import unittest

class Test(unittest.TestCase):
    def test_prod_signs(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)
        self.assertEqual(prod_signs([0, 1]), 0)
        self.assertEqual(prod_signs([]), None)

if __name__ == '__main__':
    unittest.main()