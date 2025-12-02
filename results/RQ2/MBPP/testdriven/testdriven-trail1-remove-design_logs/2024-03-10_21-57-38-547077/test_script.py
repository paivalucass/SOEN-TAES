import math

def multiply_num(numbers):
    '''
    Write a function to multiply all the numbers in a list and divide with the length of the list.
    assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
    '''

    # Input validation
    if not isinstance(numbers, (list, tuple)):
        raise ValueError('Input must be a list or a tuple')

    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError('All elements in the input must be integers or floats')

    if len(numbers) == 0:
        raise ValueError('Input list must not be empty')

    # Calculate the result
    result = 1
    for num in numbers:
        result *= num
    result /= len(numbers)

    # Return the result
    return result
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()