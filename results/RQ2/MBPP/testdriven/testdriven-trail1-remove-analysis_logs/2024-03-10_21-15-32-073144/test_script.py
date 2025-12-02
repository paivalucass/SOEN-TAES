def all_unique(test_list):
    '''
    This function checks if the elements of a given list are unique or not.
    It returns True if all elements are unique, otherwise it returns False.
    It raises specific exceptions for different types of errors.
    '''
    try:
        if isinstance(test_list, list) and len(test_list) > 0:
            return len(test_list) == len(set(test_list))
        else:
            raise ValueError("Input is not a non-empty list")
    except TypeError:
        raise TypeError("Input is not a list")
    except Exception as e:
        raise e
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_unique([1,2,3]), True)

if __name__ == '__main__':
    unittest.main()