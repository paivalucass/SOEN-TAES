def multiply_elements(input_tuple):
    # Validate input tuple has at least two elements
    if len(input_tuple) < 2:
        raise ValueError("Input tuple must have at least two elements")

    # Error handling and edge case handling
    try:
        output_tuple = tuple(input_tuple[i] * input_tuple[i+1] for i in range(len(input_tuple)-1))
    except TypeError as e:
        raise TypeError("Input tuple must contain only numbers") from e
    except IndexError as e:
        raise IndexError("Input tuple must have at least two elements") from e

    return output_tuple

import unittest

class Test(unittest.TestCase):
    def test_multiply_elements(self):
        self.assertEqual(multiply_elements((1, 5, 7, 8, 10)), (5, 35, 56, 80))

if __name__ == '__main__':
    unittest.main()