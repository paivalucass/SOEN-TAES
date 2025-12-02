def Diff(li1, li2):
    return [x for x in li1 if x not in li2]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]), [10, 20, 30, 15])

if __name__ == '__main__':
    unittest.main()