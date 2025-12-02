def new_tuple(test_list: list, test_str: str) -> tuple:
    if not isinstance(test_list, list):
        raise ValueError("test_list should be a list")
    if not isinstance(test_str, str):
        raise ValueError("test_str should be a string")
    
    return tuple(test_list + [test_str])
import unittest

class Test(unittest.TestCase):
    def test_new_tuple(self):
        self.assertEqual(new_tuple(["WEB", "is"], "best"), ('WEB', 'is', 'best'))

if __name__ == '__main__':
    unittest.main()