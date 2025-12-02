def new_tuple(test_list, test_str):
    if not isinstance(test_list, list) or not isinstance(test_str, str):
        raise TypeError("Input types are incorrect")
    if not test_list or not test_str:
        raise ValueError("List and string must not be empty")

    return tuple(test_list + [test_str])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(new_tuple(["WEB", "is"], "best"), ('WEB', 'is', 'best'))

if __name__ == '__main__':
    unittest.main()