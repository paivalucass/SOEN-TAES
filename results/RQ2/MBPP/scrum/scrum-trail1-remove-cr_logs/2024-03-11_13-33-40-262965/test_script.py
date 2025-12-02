def my_dict(input_dict):
    if not isinstance(input_dict, dict):
        raise TypeError('Input is not a dictionary')
    return bool(input_dict)
import unittest

class Test(unittest.TestCase):
    def test_empty_dictionary(self):
        self.assertEqual(my_dict({10}), False)

if __name__ == '__main__':
    unittest.main()