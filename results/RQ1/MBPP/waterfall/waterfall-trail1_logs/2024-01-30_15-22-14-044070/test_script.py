def my_dict(dict1):
    if not dict1:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(my_dict({}), True)

if __name__ == '__main__':
    unittest.main()