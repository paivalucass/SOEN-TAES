def digit_distance_nums(n1, n2):
    '''Write a python function to find the sum of the per-digit difference between two integers.
    
    Args:
    n1 (int): First integer input
    n2 (int): Second integer input
    
    Returns:
    int: Sum of the absolute differences between corresponding digits of the two numbers
    '''
    # Input validation
    if not isinstance(n1, int) or not isinstance(n2, int) or n1 < 0 or n2 < 0:
        raise ValueError("Both inputs should be non-negative integers")

    # Calculate the sum of absolute differences between corresponding digits
    result = 0
    while n1 > 0 and n2 > 0:
        digit1 = n1 % 10
        digit2 = n2 % 10
        result += abs(digit1 - digit2)
        n1 //= 10
        n2 //= 10

    # Error handling for cases where the input integers have different lengths
    if n1 > 0 or n2 > 0:
        raise ValueError("Input integers should have the same number of digits")

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digit_distance_nums(1, 2), 1)

if __name__ == '__main__':
    unittest.main()