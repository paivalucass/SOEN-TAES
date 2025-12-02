def new_tuple(test_list, test_str):
    if not isinstance(test_list, list) or not isinstance(test_str, str):
        raise TypeError("Input should be a list and a string")

    result_list = test_list.copy()
    result_list.append(test_str)
    new_tuple = tuple(result_list)
    return new_tuple
import unittest

class Test(unittest.TestCase):
    def test_new_tuple(self):
        self.assertEqual(new_tuple(["WEB", "is"], "best"), ('WEB', 'is', 'best'))

if __name__ == '__main__':
    unittest.main()