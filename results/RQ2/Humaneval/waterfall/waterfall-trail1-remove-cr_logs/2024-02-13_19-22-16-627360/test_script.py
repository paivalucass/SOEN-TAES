def iscube(a):
    if a < 0:
        a = abs(a)
    root = round(a**(1/3))
    return a == root**3
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(iscube(1))
        self.assertFalse(iscube(2))
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(0))
        self.assertFalse(iscube(180))

if __name__ == '__main__':
    unittest.main()