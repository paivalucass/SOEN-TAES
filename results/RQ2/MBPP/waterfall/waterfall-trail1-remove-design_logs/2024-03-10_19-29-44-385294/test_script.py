def find_max_element(lst):
    if not lst or not all(isinstance(element, list) for element in lst):
        return 'Error: Invalid input data format'

    max_length = 0
    max_element = None
    for sub_list in lst:
        if not all(isinstance(element, str) for element in sub_list):
            return 'Error: Invalid input data format'
        for element in sub_list:
            if len(element) > max_length:
                max_length = len(element)
                max_element = sub_list
    if max_element is not None:
        return max_element
    else:
        return 'Error: Empty list provided'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max([['A'],['A','B'],['A','B','C']]), ['A','B','C'])

if __name__ == '__main__':
    unittest.main()