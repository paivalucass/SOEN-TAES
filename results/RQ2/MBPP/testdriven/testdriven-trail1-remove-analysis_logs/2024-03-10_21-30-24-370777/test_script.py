def new_tuple(test_list, test_str):
    # Input validation
    if not isinstance(test_list, list):
        return "Error: test_list is not a list"
    if not isinstance(test_str, str):
        return "Error: test_str is not a string"
    
    # Create new tuple
    new_tuple = tuple(test_list) + (test_str,)
    
    return new_tuple
import unittest

class Test(unittest.TestCase):
    def test_new_tuple(self):
        self.assertEqual(new_tuple(["WEB", "is"], "best"), ('WEB', 'is', 'best'))

if __name__ == '__main__':
    unittest.main()