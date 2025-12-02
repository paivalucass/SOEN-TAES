def concatenate_tuple(test_tup):
    if not isinstance(test_tup, tuple):
        raise ValueError("Input parameter is not a tuple")
    concatenated_string = '-'.join(str(element) for element in test_tup)
    return concatenated_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(concatenate_tuple(("ID", "is", 4, "UTS")), 'ID-is-4-UTS')

if __name__ == '__main__':
    unittest.main()