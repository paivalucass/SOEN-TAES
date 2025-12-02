def test_duplicate(arraynums):
    '''Write a function to find whether a given array of integers contains any duplicate element.'''
    if not isinstance(arraynums, list):
        return 'Invalid Input'
    for num in arraynums:
        if not isinstance(num, int):
            return 'Invalid Input'
    unique_nums = set(arraynums)
    if len(unique_nums) == len(arraynums):
        return False
    else:
        return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_duplicate([1,2,3,4,5]), False)

if __name__ == '__main__':
    unittest.main()