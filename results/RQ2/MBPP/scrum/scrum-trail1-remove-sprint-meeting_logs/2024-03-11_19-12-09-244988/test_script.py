def tuple_str_int(test_str):
    try:
        import ast
        # Safely convert the input tuple string into a tuple
        input_tuple = ast.literal_eval(test_str)
        
        # Check if the input is a tuple
        if not isinstance(input_tuple, tuple):
            raise ValueError("Input is not a tuple")
        
        # Convert the elements of the tuple into integers
        int_tuple = tuple(int(i) for i in input_tuple)
        
        return int_tuple

    except Exception as e:
        # Handle the error and provide clear examples of how the function should handle different cases
        raise ValueError("Error:", e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_str_int('(7, 8, 9)'), (7, 8, 9))

if __name__ == '__main__':
    unittest.main()