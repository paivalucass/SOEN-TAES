def concatenate_tuple(test_tup, delimiter='-'):
    return delimiter.join(map(str, test_tup))
import unittest

class Test(unittest.TestCase):
    def test_concatenate_tuple(self):
        self.assertEqual(concatenate_tuple(("ID", "is", 4, "UTS")), 'ID-is-4-UTS')

if __name__ == '__main__':
    unittest.main()