def upper_ctr(s):
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_upper_ctr(self):
        self.assertEqual(upper_ctr('PYthon'), 2)

if __name__ == '__main__':
    unittest.main()