def concatenate_tuple(test_tup):
    return '-'.join(map(str, test_tup))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(concatenate_tuple(("ID", "is", 4, "UTS")), 'ID-is-4-UTS')

if __name__ == '__main__':
    unittest.main()