def concatenate_tuple(test_tup):
    if not isinstance(test_tup, tuple):
        raise TypeError("Input must be a tuple")

    result = '-'.join(str(i) for i in test_tup)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(concatenate_tuple(("ID", "is", 4, "UTS")), 'ID-is-4-UTS')

if __name__ == '__main__':
    unittest.main()