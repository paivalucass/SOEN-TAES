def new_tuple(test_list, test_str):
    '''Create a new tuple from the given string and list.'''
    if not test_list:
        raise ValueError("The list cannot be empty")
    if not test_str:
        raise ValueError("The string cannot be empty")
    
    new_tuple = tuple(test_list) + (test_str,)
    return new_tuple
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(new_tuple(["WEB", "is"], "best"), ('WEB', 'is', 'best'))

if __name__ == '__main__':
    unittest.main()