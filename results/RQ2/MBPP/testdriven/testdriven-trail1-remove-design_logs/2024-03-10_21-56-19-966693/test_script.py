def find_equal_tuple(input_list):
    # This function checks if all the tuples in the input list have equal length
    if not input_list:
        return False  # Return False for an empty list
    tuple_length = len(input_list[0])  # Get the length of the first tuple
    for tuple in input_list:
        if len(tuple) != tuple_length:  # Check if the length of each tuple is equal to tuple_length
            return False
    return True  # Return True if all tuples have equal length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_equal_tuple([(11, 22, 33), (44, 55, 66)]), True)

if __name__ == '__main__':
    unittest.main()