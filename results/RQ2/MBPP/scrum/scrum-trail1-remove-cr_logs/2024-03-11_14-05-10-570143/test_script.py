def new_tuple(test_list, test_str):
    if not test_list or not test_str:
        raise ValueError("Input list or string cannot be empty")
    
    new_tuple = tuple(test_list) + (test_str,)
    return new_tuple
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(new_tuple(["WEB", "is"], "best"), ('WEB', 'is', 'best'))

if __name__ == '__main__':
    unittest.main()