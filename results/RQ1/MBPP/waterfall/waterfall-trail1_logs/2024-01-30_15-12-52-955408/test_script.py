def new_tuple(test_list, test_str):
    if not isinstance(test_list, list) or not isinstance(test_str, str):
        return "Error: Invalid input"
    
    if not test_list or not test_str:
        return "Error: Invalid input"
    
    tuple_result = tuple(test_list) + (test_str,)
    
    return tuple_result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(new_tuple(["WEB", "is"], "best"), ('WEB', 'is', 'best'))

if __name__ == '__main__':
    unittest.main()