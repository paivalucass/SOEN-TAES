def Extract(lst):
    '''
    Write a python function to get the first element of each sublist.
    assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
    '''
    try:
        result = [sublist[0] for sublist in lst]
        return result
    except IndexError:
        print("Error: Sublists may have different lengths")
    except TypeError:
        print("Error: Input list contains non-list elements")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]), [1, 3, 6])

if __name__ == '__main__':
    unittest.main()