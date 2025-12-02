def smallest_num(xs):
    """
    Write a python function to find smallest number in a list.

    Args:
    xs: list of numbers

    Returns:
    smallest number in the list

    Raises:
    ValueError: if the input list is empty
    TypeError: if the input list is not numeric

    Usage:
    assert smallest_num([10, 20, 1, 45, 99]) == 1
    """
    if not xs:
        return "Input list is empty"
    
    if not all(isinstance(x, (int, float)) for x in xs):
        return "Input list should contain numeric values only"
    
    return min(xs)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(smallest_num([10, 20, 1, 45, 99]), 1)

if __name__ == '__main__':
    unittest.main()