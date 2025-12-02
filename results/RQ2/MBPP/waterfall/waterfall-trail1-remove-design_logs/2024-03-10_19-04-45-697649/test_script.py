def is_sublist(l, s):
    return all(x in l for x in s) and len(s) <= len(l) if isinstance(l, list) and isinstance(s, list) else False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_sublist([2,4,3,5,7],[3,7]), False)

if __name__ == '__main__':
    unittest.main()