def count(lst):
    '''
    Write a python function to count true booleans in the given list.
    assert count([True,False,True]) == 2
    '''
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    return sum(1 for val in lst if val)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count([True, False, True]), 2)

if __name__ == '__main__':
    unittest.main()