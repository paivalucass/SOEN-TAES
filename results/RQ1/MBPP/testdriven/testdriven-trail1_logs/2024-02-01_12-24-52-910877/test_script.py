def rear_extract(test_list):
    '''Write a function that takes in a list of tuples and returns a list containing the rear element of each tuple.
    assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]'''
    result = []
    for item in test_list:
        if not isinstance(item, tuple):
            raise TypeError("Input list contains non-tuple elements")
        result.append(item[-1])
    return result
import unittest

class Test(unittest.TestCase):
    def test_rear_extract(self):
        self.assertEqual(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]), [21, 20, 19])

if __name__ == '__main__':
    unittest.main()