def my_dict(dict1):
    if not isinstance(dict1, dict):
        raise ValueError("Input is not a dictionary")
    return not bool(dict1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(my_dict({}), True)

if __name__ == '__main__':
    unittest.main()