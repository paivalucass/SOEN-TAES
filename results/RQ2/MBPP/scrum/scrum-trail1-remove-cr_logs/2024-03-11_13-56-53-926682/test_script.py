def left_insertion(a, x):
    '''Write a function to locate the left insertion point for a specified value in sorted order.'''
    a.append(x)
    a.sort()
    return a.index(x)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(left_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()