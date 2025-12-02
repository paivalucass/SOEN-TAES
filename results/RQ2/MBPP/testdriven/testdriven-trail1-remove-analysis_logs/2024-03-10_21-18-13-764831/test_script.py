def min_val(listval):
    '''Write a function to find the minimum value in a given heterogeneous list.
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2'''
    
    if not isinstance(listval, list):
        raise TypeError("Input parameter must be a list")

    if len(listval) == 0:
        return None

    min_value = None
    for item in listval:
        if isinstance(item, int) or isinstance(item, float):
            if min_value is None or item < min_value:
                min_value = item

    return min_value
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_val(['Python', 3, 2, 4, 5, 'version']), 2)

if __name__ == '__main__':
    unittest.main()