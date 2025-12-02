def check_none(test_tup):
    if not isinstance(test_tup, tuple):
        return False
    if len(test_tup) == 0:
        return False
    for item in test_tup:
        if item is None:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_none((10, 4, 5, 6, None)), True)

if __name__ == '__main__':
    unittest.main()