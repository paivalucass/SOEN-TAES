def is_empty_dict(input_dict):
    if input_dict is None or not isinstance(input_dict, dict):
        return True
    return len(input_dict) == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(my_dict({}), True)

if __name__ == '__main__':
    unittest.main()