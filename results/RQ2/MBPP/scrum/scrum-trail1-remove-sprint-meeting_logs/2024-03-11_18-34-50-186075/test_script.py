def check_element(input_list, element):
    if not isinstance(input_list, list) or element is None:
        return "Invalid input"
    
    if not input_list:
        return False
    
    if element not in input_list:
        return False
    
    return all(item == element for item in input_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_element(['green', 'orange', 'black', 'white'], 'blue'), False)

if __name__ == '__main__':
    unittest.main()