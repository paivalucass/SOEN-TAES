def move_num(test_str):
    if not isinstance(test_str, str):
        return "Error: Invalid Input"
    
    if test_str == "":
        return test_str
    
    num_list = [char for char in test_str if char.isdigit()]
    non_num_list = [char for char in test_str if not char.isdigit()]
    
    return ''.join(non_num_list) + ''.join(num_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_num('I1love143you55three3000thousand'), 'Iloveyouthreethousand1143553000')

if __name__ == '__main__':
    unittest.main()