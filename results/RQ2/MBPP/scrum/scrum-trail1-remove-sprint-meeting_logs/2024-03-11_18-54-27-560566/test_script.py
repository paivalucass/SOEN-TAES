def my_dict(dict1):
    '''Write a function to check if a dictionary is empty'''
    if bool(dict1):
        return False
    else:
        return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(my_dict({}), True)

if __name__ == '__main__':
    unittest.main()