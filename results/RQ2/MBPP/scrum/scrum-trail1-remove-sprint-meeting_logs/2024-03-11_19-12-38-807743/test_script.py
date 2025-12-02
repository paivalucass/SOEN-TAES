def new_tuple(input_list, input_str):
    if not isinstance(input_list, list) or not isinstance(input_str, str):
        raise TypeError("Input_list should be a list and input_str should be a string")

    new_tuple = tuple(input_list + [input_str])

    return new_tuple
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(new_tuple(["WEB", "is"], "best"), ('WEB', 'is', 'best'))

if __name__ == '__main__':
    unittest.main()