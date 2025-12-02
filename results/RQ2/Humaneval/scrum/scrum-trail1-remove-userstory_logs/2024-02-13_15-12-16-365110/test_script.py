def iscube(a):
    if a < 0:
        a = -a
    return round(a ** (1/3)) ** 3 == a

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(iscube(1), True)
        self.assertEqual(iscube(2), False)
        self.assertEqual(iscube(-1), True)
        self.assertEqual(iscube(64), True)
        self.assertEqual(iscube(0), True)
        self.assertEqual(iscube(180), False)

if __name__ == '__main__':
    unittest.main()