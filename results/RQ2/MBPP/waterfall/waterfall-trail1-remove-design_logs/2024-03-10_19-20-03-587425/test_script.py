def is_dict_empty(input_dict):
    '''This function checks if a dictionary is empty'''
    return bool(input_dict)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(my_dict({10}), False)

if __name__ == '__main__':
    unittest.main()