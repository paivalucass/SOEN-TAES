def my_dict(dict1):
    if not isinstance(dict1, dict):
        raise TypeError("Input should be a dictionary")

    return bool(dict1)
import unittest

class Test(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(my_dict({10}), False)

if __name__ == '__main__':
    unittest.main()