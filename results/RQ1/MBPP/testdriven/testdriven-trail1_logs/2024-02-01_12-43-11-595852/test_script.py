def and_tuples(test_tup1, test_tup2):
    '''Write a function to extract the elementwise and tuples from the given two tuples.'''
    assert len(test_tup1) == len(test_tup2), "Input tuples must be of the same length"
    result = ()
    for i in range(len(test_tup1)):
        result += (test_tup1[i] & test_tup2[i]),
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(and_tuples((10, 4, 6, 9), (5, 2, 3, 3)), (0, 0, 2, 1))

if __name__ == '__main__':
    unittest.main()