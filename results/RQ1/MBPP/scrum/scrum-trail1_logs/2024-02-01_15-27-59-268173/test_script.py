def check_distinct(test_tup):
    '''Write a function to check if given tuple contains no duplicates'''
    if not isinstance(test_tup, tuple):
        raise TypeError("Input is not a tuple")
    if len(test_tup) == 0:
        raise ValueError("Input tuple is empty")
    
    # Convert the tuple to a set to remove duplicates
    unique_elements = set(test_tup)
    
    # Compare the length of the original tuple with the length of the set
    # If they are equal, then there are no duplicates
    return len(test_tup) == len(unique_elements)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_distinct((1, 4, 5, 6, 1, 4)), False)

if __name__ == '__main__':
    unittest.main()