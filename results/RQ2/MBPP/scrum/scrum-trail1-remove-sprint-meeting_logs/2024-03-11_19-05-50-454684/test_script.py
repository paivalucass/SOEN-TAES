def check_none(test_tup):
    if not isinstance(test_tup, tuple):
        raise ValueError("Input parameter must be a tuple")

    for value in test_tup:
        if value is None:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_none((10, 4, 5, 6, None)), True)

if __name__ == '__main__':
    unittest.main()