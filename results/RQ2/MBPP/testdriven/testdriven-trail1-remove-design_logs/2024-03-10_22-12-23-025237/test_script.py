def my_dict(input_dict):
    if not isinstance(input_dict, dict):
        return "Input must be a dictionary"
    return not bool(input_dict)
import unittest

class Test(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(my_dict({}), True)

if __name__ == '__main__':
    unittest.main()