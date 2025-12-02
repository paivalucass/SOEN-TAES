def search(arr):
    '''
    Write a python function to find the element that appears only once in a sorted array.
    assert search([1,1,2,2,3]) == 3
    '''
    result = 0
    for num in arr:
        result ^= num
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(search([1,1,2,2,3]), 3)

if __name__ == '__main__':
    unittest.main()