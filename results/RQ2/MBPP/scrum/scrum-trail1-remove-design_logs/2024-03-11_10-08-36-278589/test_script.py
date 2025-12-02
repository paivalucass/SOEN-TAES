def tup_string(tup1):
    if not isinstance(tup1, tuple):
        raise TypeError("Input should be a tuple")

    result = ''.join(str(x) for x in tup1)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')), "exercises")

if __name__ == '__main__':
    unittest.main()