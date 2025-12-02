def iscube(a):
    if not isinstance(a, int):
        return "Invalid Input"
    if a < 0:
        a = -a
    root = round(a ** (1/3))
    if (root ** 3) == a:
        return True
    else:
        return False
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