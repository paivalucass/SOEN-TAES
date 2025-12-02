def rev(num):
    return num - 1 == 2 * int(str(num)[::-1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rev(70), False)

if __name__ == '__main__':
    unittest.main()