def move_num(test_str):
    import re  
    
    if not isinstance(test_str, str):
        raise ValueError("Input must be a valid string")

    num_list = re.findall(r'\d+', test_str)  
    non_num_list = re.findall(r'\D+', test_str)  
    
    new_str = ''.join(non_num_list) + ''.join(num_list)
    
    return new_str
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_num('I1love143you55three3000thousand'), 'Iloveyouthreethousand1143553000')

if __name__ == '__main__':
    unittest.main()