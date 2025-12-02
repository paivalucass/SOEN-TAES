def test_three_equal(x, y, z):
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        raise TypeError("Inputs should be integers")
    else:
        count = 0
        if x == y == z:
            count = 3
        elif x == y or y == z or x == z:
            count = 2
        return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_three_equal(1,1,1), 3)

if __name__ == '__main__':
    unittest.main()