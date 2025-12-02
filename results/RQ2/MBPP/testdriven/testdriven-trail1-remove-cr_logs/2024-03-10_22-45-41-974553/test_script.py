def my_dict(dict1):
    if not dict1:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(my_dict({10}), False)

if __name__ == '__main__':
    unittest.main()