def list_to_float(test_list):
    if not isinstance(test_list, list):
        raise ValueError("Input must be a list")

    converted_list = []
    for sub_list in test_list:
        if not isinstance(sub_list, tuple):
            raise ValueError("Each element in the input list must be a tuple")

        new_sub_list = []
        for element in sub_list:
            try:
                new_sub_list.append(float(element))
            except ValueError:
                new_sub_list.append(element)
        converted_list.append(tuple(new_sub_list))
    
    return converted_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_to_float([( "3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")]), [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)])

if __name__ == '__main__':
    unittest.main()