def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Input:
    - l: list of integers

    Output:
    - list with elements incremented by 1
    """
    # validate input
    if not all(isinstance(i, int) for i in l):
        raise TypeError("Input must be a list of integers")

    # increment each element by 1 using list comprehension
    incremented_list = [x+1 for x in l]

    return incremented_list
import unittest

class Test(unittest.TestCase):
    def test_incr_list(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

if __name__ == '__main__':
    unittest.main()