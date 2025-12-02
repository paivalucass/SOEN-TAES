def test_three_equal(x, y, z):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int):
        return "Input is not valid"
    
    if x == y == z:
        return 3
    elif x == y or y == z or x == z:
        return 2
    else:
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_three_equal(1, 1, 1), 3)

if __name__ == '__main__':
    unittest.main()