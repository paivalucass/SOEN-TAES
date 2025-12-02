def list_to_float(test_list):
    '''
    Write a function to convert all possible convertible elements in a list of lists to floats.
    assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
    '''

    modified_list = []
    for sublist in test_list:
        try:
            converted_sublist = [float(elem) for elem in sublist]
            modified_list.append(tuple(converted_sublist))
        except ValueError as e:
            # Log the error and skip the non-convertible elements
            print(f"Error converting elements: {e}")
            continue
    
    return modified_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_to_float([( "3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")]), [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)])

if __name__ == '__main__':
    unittest.main()