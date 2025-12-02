def tup_string(tup1):
    return ''.join(str(x) for x in tup1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')), "exercises")

if __name__ == '__main__':
    unittest.main()