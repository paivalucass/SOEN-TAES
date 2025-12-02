def count(lst):
    if not isinstance(lst, list):
        return 0
    if not lst:
        return 0
    return lst.count(True)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count([True, False, True]), 2)

if __name__ == '__main__':
    unittest.main()