def tuple_str_int(test_str):
    if test_str == "":
        return ()
    if test_str[0] != '(' or test_str[-1] != ')':
        raise ValueError("Input string must start with '(' and end with ')'")
    
    test_str = test_str[1:-1]  
    int_list = [int(x) for x in test_str.split(',')]  
    return tuple(int_list)  
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_str_int("(7, 8, 9)"), (7, 8, 9))

if __name__ == '__main__':
    unittest.main()