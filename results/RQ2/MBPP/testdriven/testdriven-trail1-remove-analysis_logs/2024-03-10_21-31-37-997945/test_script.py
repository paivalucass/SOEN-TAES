def empty_dit(list1):
    '''
    Write a function to check whether all dictionaries in a list are empty or not.
    assert empty_dit([{},{},{}])==True
    '''
    for dictionary in list1:
        if not isinstance(dictionary, dict):
            return False
        if bool(dictionary):
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(empty_dit([{}, {}, {}]), True)

if __name__ == '__main__':
    unittest.main()