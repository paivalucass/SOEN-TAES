def volume_cube(l):
    if not isinstance(l, (int, float)):
        raise TypeError("The side length should be a number")
    if l <= 0:
        raise ValueError("The side length should be a positive number")
        
    return l ** 3
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(volume_cube(3), 27)

if __name__ == '__main__':
    unittest.main()