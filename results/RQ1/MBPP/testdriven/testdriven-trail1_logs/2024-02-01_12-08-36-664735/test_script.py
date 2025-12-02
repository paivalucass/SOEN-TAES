def tup_string(tup1):
    if not isinstance(tup1, tuple):
        raise ValueError("Input must be a tuple")
    return ''.join(tup1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')), "exercises")

if __name__ == '__main__':
    unittest.main()