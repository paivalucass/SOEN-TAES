def lateralsurface_cube(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Input side length must be a number")
    
    if side_length < 0:
        return 0
    
    return 4 * (side_length ** 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lateralsurface_cube(5), 100)

if __name__ == '__main__':
    unittest.main()