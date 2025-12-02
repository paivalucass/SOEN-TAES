def check_element(input_list, element):
    '''
    Write a function that takes in a list and element and checks whether all items in the list are equal to the given element.
    '''
    if not isinstance(input_list, list) or not input_list:
        return "Error"
    for item in input_list:
        if item != element:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_check_element(self):
        self.assertEqual(check_element(["green", "orange", "black", "white"], 'blue'), False)

if __name__ == '__main__':
    unittest.main()