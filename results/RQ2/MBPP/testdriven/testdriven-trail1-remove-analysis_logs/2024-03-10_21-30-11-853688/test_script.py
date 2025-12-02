def tuple_str_int(test_str):
    try:
        # Remove parentheses and split input string by comma
        split_strings = test_str.replace('(', '').replace(')', '').split(',')
        
        # Convert each split string to an integer and store in a new tuple
        new_tuple = tuple(int(num) for num in split_strings)
        
        # Return the new tuple of integers
        return new_tuple
    except ValueError:
        raise ValueError("Invalid input string format")

# Testing the function
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_str_int("(7, 8, 9)"), (7, 8, 9))

if __name__ == '__main__':
    unittest.main()