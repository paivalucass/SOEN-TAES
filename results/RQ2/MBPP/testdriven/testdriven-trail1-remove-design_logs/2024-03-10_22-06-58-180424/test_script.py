def remove_odd(l):
    '''
    Write a python function to remove odd numbers from a given list.
    assert remove_odd([1,2,3]) == [2]
    '''
    if not isinstance(l, list):
        raise TypeError("Input must be a list of integers")

    if not all(isinstance(x, int) for x in l):
        raise ValueError("Input must be a list of integers")

    return [x for x in l if x % 2 == 0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_odd([1,2,3]), [2])

if __name__ == '__main__':
    unittest.main()