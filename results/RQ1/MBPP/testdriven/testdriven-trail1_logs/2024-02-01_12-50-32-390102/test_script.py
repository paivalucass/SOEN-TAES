def Extract(lst):
    '''
    Write a python function to get the first element of each sublist.
    assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
    '''
    if not all(isinstance(sublist, list) for sublist in lst):
        raise ValueError("Input must be a list of lists")

    result = [sublist[0] for sublist in lst]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]), [1, 3, 6])

if __name__ == '__main__':
    unittest.main()