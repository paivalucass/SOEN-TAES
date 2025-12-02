def sum_list(lst1, lst2):
    '''
    This function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
    It also validates the input lists to ensure they have the same length and only contain integers.
    '''

    # Input validation for empty lists
    if not lst1 or not lst2:
        raise ValueError("Input lists cannot be empty")

    # Check for lists with different lengths
    if len(lst1) != len(lst2):
        raise ValueError("Input lists must have the same length")

    # Check for non-integer elements in the lists
    if not all(isinstance(x, int) for x in lst1) or not all(isinstance(x, int) for x in lst2):
        raise ValueError("Input lists must only contain integers")

    # Return the sum of the two lists
    return [x + y for x, y in zip(lst1, lst2)]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_list([10, 20, 30], [15, 25, 35]), [25, 45, 65])

if __name__ == '__main__':
    unittest.main()