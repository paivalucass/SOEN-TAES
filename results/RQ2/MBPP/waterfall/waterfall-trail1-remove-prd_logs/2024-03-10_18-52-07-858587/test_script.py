def my_dict(dict1):
    if dict1 is None or not isinstance(dict1, dict):
        raise ValueError("Input is not a valid dictionary")
    return len(dict1) == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(my_dict({}), True)

if __name__ == '__main__':
    unittest.main()