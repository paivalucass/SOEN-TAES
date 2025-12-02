def find_tuples(test_list: list[tuple], K: int) -> list[tuple]:
    '''
    Write a function to find tuples which have all elements divisible by K from the given list of tuples.
    
    Args:
    - test_list: List of tuples
    - K: Integer
    
    Returns:
    - List of tuples which have all elements divisible by K
    
    Example:
    assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
    '''
    # Input validation
    if not all(isinstance(t, tuple) for t in test_list) or not isinstance(K, int):
        raise ValueError("Input validation failed. test_list must be a list of tuples and K must be an integer.")
    
    # List comprehension for concise implementation
    result = [t for t in test_list if all(i % K == 0 for i in t)]
    
    return result

import unittest

class Test(unittest.TestCase):
    def test_find_tuples(self):
        self.assertEqual(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6), [(6, 24, 12)])

if __name__ == '__main__':
    unittest.main()