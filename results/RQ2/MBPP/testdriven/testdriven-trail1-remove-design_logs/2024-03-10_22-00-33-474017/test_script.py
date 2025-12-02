def frequency(a, x):
    return a.count(x) if x in a else 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency([1,2,3], 4), 0)

if __name__ == '__main__':
    unittest.main()