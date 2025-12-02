def remove_odd(l):
    '''Write a python function to remove odd numbers from a given list.'''
    even_numbers = [x for x in l if x % 2 == 0]
    return even_numbers

# Test cases
assert remove_odd([1, 2, 3]) == [2]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_odd([1,2,3]), [2])

if __name__ == '__main__':
    unittest.main()