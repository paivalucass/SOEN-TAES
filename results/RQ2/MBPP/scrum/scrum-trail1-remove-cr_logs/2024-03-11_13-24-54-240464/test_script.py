def upper_ctr(str):
    count = sum(1 for char in str if char.isupper())
    return count
import unittest

class Test(unittest.TestCase):
    def test_upper_ctr(self):
        self.assertEqual(upper_ctr('PYthon'), 2)

if __name__ == '__main__':
    unittest.main()