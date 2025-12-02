def find_equal_tuple(input_list_of_tuples):
    '''
    Write a function to find whether all the given tuples have equal length or not.

    Parameters:
    input_list_of_tuples (list): The input will be a list of tuples.

    Returns:
    bool: The output will be a boolean value indicating whether all the tuples have equal length or not.
    '''

    # Check for invalid input
    if not isinstance(input_list_of_tuples, list) or not all(isinstance(item, tuple) for item in input_list_of_tuples):
        raise TypeError("Input should be a list of tuples")

    # Check for equal length of tuples
    tuple_length = len(input_list_of_tuples[0])
    if all(len(item) == tuple_length for item in input_list_of_tuples):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_equal_tuple([(11, 22, 33), (44, 55, 66)]), True)

if __name__ == '__main__':
    unittest.main()