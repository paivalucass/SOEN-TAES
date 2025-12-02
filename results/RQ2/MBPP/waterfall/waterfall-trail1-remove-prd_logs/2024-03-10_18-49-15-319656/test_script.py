def tuple_str_int(test_str):
    if not is_valid_input(test_str):
        return "Error: Invalid input format"

    elements = test_str.strip('()').split(',')
    
    int_elements = [int(element) for element in elements]
    
    result = tuple(int_elements)
    
    return result

def is_valid_input(test_str):
    if test_str[0] != "(" or test_str[-1] != ")":
        return False
    
    elements = test_str[1:-1].split(',')
    for element in elements:
        if not element.strip().isdigit():
            return False
    
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_str_int("(7, 8, 9)"), (7, 8, 9))

if __name__ == '__main__':
    unittest.main()