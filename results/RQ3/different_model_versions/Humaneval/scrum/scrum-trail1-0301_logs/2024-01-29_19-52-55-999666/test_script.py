def has_pair_summing_to_zero(numbers):
    """
    has_pair_summing_to_zero takes a list of integers as an input.
    It returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Use set to store already evaluated numbers, reducing iterations
    numbers_set = set(numbers)
    for num in numbers:
        if -num in numbers_set:
            # Return True if a pair is found
            return True
    # Return False if no pair is found
    return False

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    It returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Check if input is a list
    if not isinstance(l, list):
        raise TypeError("Input must be a list")
    
    # Check if input list contains only integers
    if not all(isinstance(num, int) for num in l):
        raise TypeError("Input list must contain only integers")
    
    # Call has_pair_summing_to_zero function and return its result
    return has_pair_summing_to_zero(l)
import unittest

class TestPairsSumToZero(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(pairs_sum_to_zero([]), False)
        
    def test_single_element_list(self):
        self.assertEqual(pairs_sum_to_zero([1]), False)
        
    def test_no_sum_to_zero(self):
        self.assertEqual(pairs_sum_to_zero([1, 3, 5, 7]), False)
        
    def test_one_sum_to_zero(self):
        self.assertEqual(pairs_sum_to_zero([1, -1]), True)
        
    def test_multiple_sum_to_zero(self):
        self.assertEqual(pairs_sum_to_zero([1, 2, -3, 4, -2]), True)

if __name__ == '__main__':
    unittest.main()