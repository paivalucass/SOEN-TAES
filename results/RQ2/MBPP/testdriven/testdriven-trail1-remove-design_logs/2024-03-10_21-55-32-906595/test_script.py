def test_duplicate(arraynums):
    '''
    Write a function to find whether a given array of integers contains any duplicate element.
    '''
    # Check if the length of the array is not equal to the length of the set of the array
    return len(arraynums) != len(set(arraynums))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_duplicate([1,2,3,4,5]), False)

if __name__ == '__main__':
    unittest.main()