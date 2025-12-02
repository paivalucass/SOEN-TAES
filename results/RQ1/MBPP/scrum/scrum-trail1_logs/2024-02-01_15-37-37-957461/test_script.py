def concatenate_tuple(test_tup, delimiter='-'):
    if isinstance(test_tup, tuple):
        concatenated_string = delimiter.join(map(str, test_tup))
        return concatenated_string
    else:
        return "Error: Input is not a tuple"
import unittest

class Test(unittest.TestCase):
    def test_concatenate_tuple(self):
        self.assertEqual(concatenate_tuple(("ID", "is", 4, "UTS")), 'ID-is-4-UTS')

if __name__ == '__main__':
    unittest.main()