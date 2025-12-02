def similar_elements(list1, list2):
    '''Write a function to find the shared elements from the given two lists.'''
    return set(list1) & set(list2)

assert similar_elements((3, 4, 5, 6),(5, 7, 4, 10)) == {4, 5}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(similar_elements((3, 4, 5, 6), (5, 7, 4, 10)), {4, 5})

if __name__ == '__main__':
    unittest.main()