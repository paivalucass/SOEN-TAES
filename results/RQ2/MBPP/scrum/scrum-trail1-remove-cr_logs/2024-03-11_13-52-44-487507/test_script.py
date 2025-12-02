def heap_sort(iterable):
    '''Write a function to sort the given list.'''
    return sorted(iterable)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()