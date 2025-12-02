def maximize_elements(test_tup1, test_tup2):
    '''Write a function to maximize the given two tuples.'''
    max_values = ()
    for i in range(min(len(test_tup1), len(test_tup2))):
        max_values += (max(test_tup1[i][0], test_tup2[i][0]), max(test_tup1[i][1], test_tup2[i][1])),
    return max_values
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))), 
                         ((6, 7), (4, 9), (2, 9), (7, 10)))

if __name__ == '__main__':
    unittest.main()