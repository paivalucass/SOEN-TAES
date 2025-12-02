def count(boolean_list):
    return boolean_list.count(True)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count([True, False, True]), 2)

if __name__ == '__main__':
    unittest.main()