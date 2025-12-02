def check_type(test_tuple):
    '''Write a function to check if all the elements in tuple have the same data type or not.'''
    if len(test_tuple) == 0 or len(test_tuple) == 1:
        return True
    else:
        return all(isinstance(x, type(test_tuple[0])) for x in test_tuple)

import unittest

class Test(unittest.TestCase):
    def test_check_type(self):
        self.assertEqual(check_type((5, 6, 7, 3, 5, 6)), True)

if __name__ == '__main__':
    unittest.main()