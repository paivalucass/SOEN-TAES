def list_to_float(test_list):
    if not test_list:
        raise ValueError("Error: Input list is empty")
    
    modified_list = []
    for sublist in test_list:
        temp = []
        for element in sublist:
            try:
                temp.append(float(element))
            except ValueError:
                raise ValueError("Error: Non-convertible elements present")
        modified_list.append(tuple(temp))
    return modified_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_to_float([( "3", "4" ), ( "1", "26.45" ), ( "7.32", "8" ), ( "4", "8" )]), [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)])

if __name__ == '__main__':
    unittest.main()