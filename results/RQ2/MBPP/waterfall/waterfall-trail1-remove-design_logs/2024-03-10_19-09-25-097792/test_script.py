def volume_cube(l):
    if not isinstance(l, (int, float)):
        raise ValueError("Input must be a valid number")
    if l <= 0:
        raise ValueError("Error: Invalid input, side length should be a positive integer")
    
    return l ** 3
import unittest

class Test(unittest.TestCase):
    def test_volume_cube(self):
        self.assertEqual(volume_cube(3), 27)

if __name__ == '__main__':
    unittest.main()