def Extract(lst):
    result = [sublist[0] for sublist in lst if sublist]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]), [1, 3, 6])

if __name__ == '__main__':
    unittest.main()