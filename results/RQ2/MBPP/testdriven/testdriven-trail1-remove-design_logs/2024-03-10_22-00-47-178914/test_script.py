def check_type(test_tuple):
    '''
    Write a function to check if all the elements in tuple have the same data type or not.
    assert check_type((5, 6, 7, 3, 5, 6) ) == True
    '''
    if all(isinstance(element, type(test_tuple[0])) for element in test_tuple):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test_check_type(self):
        self.assertEqual(check_type((5, 6, 7, 3, 5, 6)), True)

if __name__ == '__main__':
    unittest.main()